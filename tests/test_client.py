import unittest
import requests_mock
from . import fixtures

from src.agify.client import AgifyAPIClient
from src.agify.client import NameData


class TestAgifyApiClient(unittest.TestCase):
    @requests_mock.Mocker()
    def test_client_success(self, reqmock):
        reqmock.get(AgifyAPIClient.base_url, json=fixtures.CLIENT_SUCCESS)
        data = AgifyAPIClient.fetch('test')
        assert isinstance(data, NameData)

    @requests_mock.Mocker()
    def test_client_no_data(self, reqmock):
        reqmock.get(AgifyAPIClient.base_url, json=fixtures.CLIENT_NO_DATA)
        data = AgifyAPIClient.fetch('testpqwoieru')
        assert isinstance(data, NameData)
