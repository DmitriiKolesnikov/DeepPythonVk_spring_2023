import argparse
import asyncio
import json
import operator

import aiohttp


async def fetch_url(session, url):
    async with session.get(url) as response:
        return await response.text()

async def process_url(session, url, results_queue):
    text = await fetch_url(session, url)
    words = re.findall(r'\w+', text.lower())
    word_counts = {}
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    sorted_word_counts = sorted(word_counts.items(), key=operator.itemgetter(1), reverse=True)[:top_k]
    result = {word: count for word, count in sorted_word_counts}
    results_queue.put((url, result))

async def handle_responses(results_queue):
    while True:
        url, result = await results_queue.get()
        print(f'{url}: {result}')
        results_queue.task_done()

async def main(urls_file, num_tasks):
    async with aiohttp.ClientSession() as session:
        results_queue = asyncio.Queue()
        urls = []
        with open(urls_file) as f:
            urls = f.read().splitlines()
        tasks = []
        for url in urls:
            task = asyncio.ensure_future(process_url(session, url, results_queue))
            tasks.append(task)

        results_task = asyncio.ensure_future(handle_responses(results_queue))
        await asyncio.gather(*tasks)
        await results_queue.join()
        results_task.cancel()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('num_tasks', type=int, help='Number of concurrent tasks')
    parser.add_argument('urls_file', type=str, help='Path to file with URLs')
    args = parser.parse_args()

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(args.urls_file, args.num_tasks))
