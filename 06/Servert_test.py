
from Server import *
import asyncio
import json
import time
import operator
import re
import unittest
import urllib.parse
from http.server import HTTPServer, BaseHTTPRequestHandler
from multiprocessing import Process

from aiohttp import ClientSession

from server import WordCountServer
from client import RequestException, fetch_url, process_url, handle_responses


class TestServer(unittest.TestCase):

    def setUp(self):
        self.loop = asyncio.new_event_loop()
        asyncio.set_event_loop(None)

    def tearDown(self):
        self.loop.close()

    def test_serve(self):
        test_server = WordCountServer(loop=self.loop, listen='127.0.0.1', port=8080)
        self.loop.run_until_complete(test_server.serve())
        test_server.close()

    def test_handle_request(self):

        class MockRequestHandler(BaseHTTPRequestHandler):
            protocol_version = 'HTTP/1.1'

            def do_POST(self):

                length = int(self.headers.get('content-length'))
                data = self.rfile.read(length)
                url = data.decode().strip()

                async def mock_fetch_url(url):
                    return 'test text\n'

                result = self.server.process_url(url, mock_fetch_url)
                json_result = json.dumps(result)
                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.send_header('Content-Length', len(json_result))
                self.end_headers()

                self.wfile.write(json_result.encode())

        server = HTTPServer(('127.0.0.1', 8080), MockRequestHandler)
        server.process_url = lambda url, fetch_url: {"the": 1, "quick": 1, "brown": 1, "fox": 1}
        process = Process(target=server.serve_forever)
        process.start()

        while True:
            try:
                response = urllib.request.urlopen('http://127.0.0.1:8080')
                break
            except urllib.error.URLError:
                time.sleep(0.1)

        with self.subTest("Valid URL"):
            url = 'http://example.com/text.txt'
            req = urllib.request.Request('http://127.0.0.1:8080', data=url.encode())
            response = urllib.request.urlopen(req)
            self.assertEqual(response.status, 200)
            self.assertEqual(json.loads(response.read()), {"the": 1, "quick": 1, "brown": 1, "fox": 1})

        with self.subTest("Invalid URL"):
            url = 'not_a_url'
            req = urllib.request.Request('http://127.0.0.1:8080', data=url.encode())
            with self.assertRaises(HTTPError):
                urllib.request.urlopen(req)

        with self.subTest("Empty URL"):
            url = ''
            req = urllib.request.Request('http://127.0.0.1:8080', data=url.encode())
            with self.assertRaises(HTTPError):
                urllib.request.urlopen(req)

        server.shutdown()
        process.join(1)

        if process.is_alive():
            process.terminate()
            process.join()

    def test_handle_request_timeout(self):

        class MockRequestHandler(BaseHTTPRequestHandler):
            protocol_version = 'HTTP/1.1'

            def do_POST(self):

                length = int(self.headers.get('content-length'))
                data = self.rfile.read(length)
                url = data.decode().strip()

                async def mock_fetch_url(url):
                    time.sleep(0.5)
                    return 'test text\n'

                result = self.server.process_url(
                    url,
                    mock_fetch_url,
                    request_timeout=0.1
                )
                json_result = json.dumps(result)
                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.send_header('Content-Length', len(json_result))
                self.end_headers()

                self.wfile.write(json_result.encode())

        server = HTTPServer(('127.0.0.1', 8080), MockRequestHandler)
        process = Process(target=server.serve_forever)
        process.start()

        while True:
            try:
                response = urllib.request.urlopen('http://127.0.0.1:8080')
                break
            except urllib.error.URLError:
                time.sleep(0.1)

        with self.subTest("Timeout"):
            url = 'http://example.com/text.txt'
            req = urllib.request.Request('http://127.0.0.1:8080', data=url.encode())
            with self.assertRaises(HTTPError):
                urllib.request.urlopen(req)

        server.shutdown()
        process.join(1)

        if process.is_alive():
            process.terminate()
            process.join()

if __name__ == "__main__":
  unittest.main()
