import unittest
import asyncio
from unittest.mock import patch, MagicMock
from Script import fetch_urls


class TestFetchUrls(unittest.TestCase):
    @patch('Script.aiohttp.ClientSession')
    def test_fetch_urls(self, mock_session):
        urls_file = 'urls.txt'
        concurrent_requests = 10
        mock_response = MagicMock()
        mock_response.text.return_value = '<html></html>'
        mock_session.return_value.__aenter__ = MagicMock(return_value=mock_session.return_value)
        mock_session.return_value.get.return_value = asyncio.Future()
        mock_session.return_value.get.return_value.set_result(mock_response)
        loop = asyncio.get_event_loop()
        responses = loop.run_until_complete(fetch_urls(urls_file, concurrent_requests))
        self.assertEqual(len(responses), 1)
        self.assertEqual(responses[0], '<html></html>')


