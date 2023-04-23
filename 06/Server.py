import socket
import urllib.request
from collections import Counter
import re

BUFFER_SIZE = 4096


def count_words(url):
    response = urllib.request.urlopen(url)
    html = response.read()
    words = re.findall(r'\w+', html.decode())
    return Counter(words)


def format_response(words_count):
    sorted_words = sorted(words_count.items(), key=lambda x: x[1], reverse=True)
    response = '\n'.join([f'{w}: {c}' for w, c in sorted_words])
    return response


def start_server(host='127.0.0.1', port=65432):

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        print(f'Server started on {host}:{port}')

        while True:
            conn, addr = s.accept()
            with conn:
                print('Connected by', addr)
                url = conn.recv(BUFFER_SIZE).decode()
                try:
                    words_count = count_words(url)
                    response = format_response(words_count)
                except Exception as e:
                    response = f'Error: {str(e)}'
                conn.sendall(response.encode())


if __name__ == "__main__":
    print("Server")


