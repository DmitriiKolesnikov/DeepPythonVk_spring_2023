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
            
            
class TestProcessUrl1(unittest.IsolatedAsyncioTestCase):
    async def test_process_url(self):
        mock_response = MagicMock()
        mock_response.text.return_value = "test"

        mock_get = MagicMock()
        mock_get.return_value.__aenter__.return_value = mock_response

        with patch.object(aiohttp.ClientSession, 'get', new=mock_get):
            session = aiohttp.ClientSession()
            response = await code.process_url(session, "http://example.com")

        self.assertEqual(response, "test")
        mock_get.assert_called_once_with("http://example.com")
        mock_response.text.assert_called_once()

        
class TestFetchUrls1(unittest.IsolatedAsyncioTestCase):
    async def test_fetch_urls(self):
        mock_response1 = MagicMock()
        mock_response1.text.return_value = "test1"

        mock_response2 = MagicMock()
        mock_response2.text.return_value = "test2"

        mock_get = MagicMock()
        mock_get.side_effect = [mock_response1, mock_response2]

        with patch.object(aiohttp.ClientSession, 'get', new=mock_get):
            result = await code.fetch_urls('urls.txt', 2)

        self.assertEqual(len(result), 2)
        self.assertEqual(result, ["test1", "test2"])
        mock_get.assert_has_calls([mock.call("http://example.com"), mock.call("http://test.com/")])
        mock_response1.text.assert_called_once()
        mock_response2.text.assert_called_once()


if __name__ == "__main__":
    unittest.main()
