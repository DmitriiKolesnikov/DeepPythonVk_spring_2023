import argparse
import asyncio
import json
import operator
import re
import threading

import aiohttp


class WorkerThread(threading.Thread):
    def __init__(self, worker_id, url_queue, top_k, results_queue):
        super().__init__()
        self.id = worker_id
        self.url_queue = url_queue
        self.top_k = top_k
        self.results_queue = results_queue

    async def process_url(self, session, url):
        async with session.get(url) as response:
            return await response.text()

    async def handle_request(self, session, url):
        text = await self.process_url(session, url)
        words = re.findall(r'\w+', text.lower())
        word_counts = {}
        for word in words:
            if word in word_counts:
                word_counts[word] += 1
            else:
                word_counts[word] = 1
        sorted_word_counts = sorted(word_counts.items(), key=operator.itemgetter(1), reverse=True)[:self.top_k]
        result = {word: count for word, count in sorted_word_counts}
        self.results_queue.put(result)

    async def run(self):
        async with aiohttp.ClientSession() as session:
            while True:
                url = await self.url_queue.get()
                await self.handle_request(session, url)
                self.url_queue.task_done()


async def serve_forever(worker_count, top_k):
    url_queue = asyncio.Queue()
    results_queue = asyncio.Queue()
    workers = [WorkerThread(i, url_queue, top_k, results_queue) for i in range(worker_count)]

    for worker in workers:
        worker.start()

    async def handle_client(reader, writer):
        while True:
            data = await reader.readline()
            if not data:
                break
            url = data.decode().strip()
            url_queue.put_nowait(url)

        url_queue.join()

        result = {}
        while not results_queue.empty():
            result.update(results_queue.get())

        writer.write(json.dumps(result).encode() + b'\n')
        await writer.drain()
        writer.close()

    server = await asyncio.start_server(handle_client, '127.0.0.1', 8080)

    async with server:
        await server.serve_forever()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-w', '--workers', type=int, default=1, help='Number of worker threads')
    parser.add_argument('-k', '--top-k', type=int, default=10, help='Number of top words to return')
    args = parser.parse_args()

    loop = asyncio.get_event_loop()
    loop.run_until_complete(serve_forever(args.workers, args.top_k))
