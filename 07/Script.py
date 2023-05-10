
import aiohttp
import asyncio
import argparse


async def process_url(session, url):
    async with session.get(url) as response:
        return await response.text()


async def fetch_urls(urls_file, concurrent_requests):
    async with aiohttp.ClientSession() as session:
        sem = asyncio.Semaphore(concurrent_requests)
        tasks = []
        with open(urls_file) as f:
            urls = f.read().splitlines()
        for url in urls:
            await sem.acquire()
            task = asyncio.ensure_future(process_url(session, url))
            task.add_done_callback(lambda t: sem.release())
            tasks.append(task)
        responses = await asyncio.gather(*tasks)
        return responses


if "__name__" == "main":
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--concurrent', type=int, default=10, help='Number of concurrent requests')
    parser.add_argument('urls_file', type=str, help='Path to file with URLs')
    args = parser.parse_args()

    loop = asyncio.get_event_loop()
    responses = loop.run_until_complete(fetch_urls(args.urls_file, args.concurrent))
    for response in responses:
        print(response)

