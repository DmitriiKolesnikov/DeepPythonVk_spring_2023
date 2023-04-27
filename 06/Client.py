import socket
import threading
import json
import argparse

def process_url(url):
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(('localhost', 8000))
        client_socket.send(url.encode('utf-8'))
        response = client_socket.recv(1024).decode('utf-8')
        print(f"{url}: {response}")
    except Exception as e:
        print(f"Error processing URL {url}: {str(e)}")
    finally:
        client_socket.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Client for sending requests to master-worker server')
    parser.add_argument('urls_file', type=str, help='File containing URL list')
    parser.add_argument('-m', '--threads', type=int, default=1, help='Number of threads (default 1)')
    args = parser.parse_args()

    with open(args.urls_file) as f:
        urls = f.readlines()

    urls = [url.strip() for url in urls]

    for i in range(0, len(urls), args.threads):
        threads = []
        for j in range(args.threads):
            if i + j < len(urls):
                url = urls[i+j]
                t = threading.Thread(target=process_url, args=(url,))
                t.start()
                threads.append(t)
        for t in threads:
            t.join()
