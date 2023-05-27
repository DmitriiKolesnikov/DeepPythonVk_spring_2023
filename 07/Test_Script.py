import unittest
from unittest.mock import MagicMock, patch
import asyncio
import aiohttp

from Script import process_url, fetch_urls


class TestProcessUrl(unittest.IsolatedAsyncioTestCase):
    async def test_process_url(self):
        with patch("aiohttp.ClientSession.get") as mock:
            url = "http://test.com/"
            response_mock = MagicMock()

            response_mock.text.return_value = "test"
            mock.return_value.__aenter__.return_value = response_mock

            session = aiohttp.ClientSession()
            response = await process_url(session, url)
            self.assertEqual(response, "test")
            mock.assert_called_once()
            response_mock.text.assert_called_once()


class TestFetchUrls(unittest.IsolatedAsyncioTestCase):
    async def test_fetch_urls(self):
        with patch("code.process_url") as mock:
            urls_file = "/path/to/urls/file",
            concurrent_requests = 5,
            response_mock = MagicMock()

            response_mock.text.return_value = "test"
            mock.return_value = response_mock

            session = aiohttp.ClientSession()
            result = await fetch_urls(urls_file, concurrent_requests)
            mock.assert_called()
            self.assertEqual(len(result), 1)


if __name__ == "__main__":
    unittest.main()
