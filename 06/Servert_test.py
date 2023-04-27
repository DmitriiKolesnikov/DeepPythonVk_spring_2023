
import unittest
from Server import *


class TestServer(unittest.TestCase):

  def test_dispatch_work():
      server = MasterWorkerServer('localhost', 8000, 10, 7)
      client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      client_socket.connect(('localhost', 8000))
      url = 'https://ru.wikipedia.org/wiki/Baba_Yaga'
      server.dispatch_work(url, client_socket)
      assert server.task_queue.get() == (url, client_socket)

  def test_worker_loop():
      server = MasterWorkerServer('localhost', 8000, 10, 7)
      url = 'https://ru.wikipedia.org/wiki/Baba_Yaga'
      client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      server.task_queue.put((url, client_socket))
      server.worker_loop()
      response = client_socket.recv(1024).decode('utf-8')
      assert isinstance(json.loads(response), dict)

  def test_start():
      server = MasterWorkerServer('localhost', 8000, 10, 7)
      t = threading.Thread(target=server.start)
      t.start()
      time.sleep(1)
      client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      client_socket.connect(('localhost', 8000))
      url = 'http://example.com'
      client_socket.send(url.encode('utf-8'))
      response = client_socket.recv(1024).decode('utf-8')
      assert isinstance(json.loads(response), dict)
      
      
if __name__ = "__main__":
  unittest.main()

