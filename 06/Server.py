import socket
import threading
import json
import urllib.request
from collections import Counter


class MasterWorkerServer:
    def __init__(self, host, port, num_workers, top_k):
        self.host = host
        self.port = port
        self.num_workers = num_workers
        self.top_k = top_k
        self.worker_threads = []
        self.url_counter = 0

    def start(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((self.host, self.port))
        self.socket.listen(1)
        print(f"Server listening on {self.host}:{self.port} with {self.num_workers} workers.")

        for i in range(self.num_workers):
            t = threading.Thread(target=self.worker_loop)
            t.start()
            self.worker_threads.append(t)

        while True:
            client_socket, addr = self.socket.accept()
            print(f"Accepted connection from {addr}")
            url = client_socket.recv(1024).decode()
            print(f"Received URL: {url}")
            self.dispatch_work(url, client_socket)

    def dispatch_work(self, url, client_socket):
        self.task_queue.put((url, client_socket))

    def worker_loop(self):
        while True:
            url, client_socket = self.task_queue.get()
            try:
                response = urllib.request.urlopen(url)
                data = response.read().decode('utf-8')
                words = data.split()
                counter = Counter(words)
                top_k_words = dict(counter.most_common(self.top_k))
                client_socket.send(json.dumps(top_k_words).encode('utf-8'))
            except Exception as e:
                print(f"Error processing URL {url}: {str(e)}")
            finally:
                client_socket.close()
                self.url_counter += 1
                print(f"Processed {self.url_counter} URLs")

                
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Master-worker server for processing client requests')
    parser.add_argument('-w', '--workers', type=int, default=10, help='Number of worker threads (default 10)')
    parser.add_argument('-k', '--top_k', type=int, default=7, help='Top K most common words to return (default 7)')
    args = parser.parse_args()
    server = MasterWorkerServer('localhost', 8000, args.workers, args.top_k)
    server.start()

