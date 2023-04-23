import socket

BUFFER_SIZE = 4096


def get_top_words(url):
    host = '127.0.0.1'
    port = 65432

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        s.sendall(url.encode())
        data = s.recv(BUFFER_SIZE).decode()
        return data


if __name__ == "__main__":
    print("Client")