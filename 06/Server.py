import socket
import threading
import urllib.request
import json
from collections import Counter


def worker(worker_id):
    urls_processed = 0
    while True:
        try:
            url, client_socket = master_queue.get()
        except:
            print(f"Worker {worker_id} finished. Processed {urls_processed} urls.")
            return
        try:
            response = urllib.request.urlopen(url)
            html = response.read().decode()
            words = html.split()
            top_k_words = dict(Counter(words).most_common(k))
            json_data = json.dumps(top_k_words)
            client_socket.sendall(json_data.encode())
        except:
            
            client_socket.sendall(b"Error")
        finally:
            client_socket.close()
            urls_processed += 1
            print(f"Worker {worker_id} processed {url}. Total processed: {urls_processed}")


master_queue = queue.Queue()
num_workers = 4
for i in range(num_workers):
    threading.Thread(target=worker, args=(i,)).start()
host = ""
port = 12345
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(5)
while True:
    client_socket, addr = s.accept()
    url = client_socket.recv(1024).decode()
    master_queue.put((url, client_socket))
