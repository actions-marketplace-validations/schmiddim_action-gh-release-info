import json
from modules.releases import _get_data_from_api, _get_api_url_for_repo
from modules.releases import _get_latest_tag, _get_asset_download_url_by_pattern
from modules.releases import get_tag_and_download_url
from argparse import Namespace

from main import main
import requests_mock.mocker


class TestReleases:

    def test_api_release_url(self):
        for test in TestReleases._get_test_table():
            got = _get_api_url_for_repo(test.get("repo_url"))
            assert got == test.get("want_release_url")

    def test_get_tag(self):
        for test in TestReleases._get_test_table():
            data = TestReleases._load_json_fixture(test.get("path"))
            want = test.get("tag")
            got = _get_latest_tag(data)
            assert got == want

    def test_assets(self, requests_mock: requests_mock.mocker.Mocker):
        for test in TestReleases._get_test_table():
            response = TestReleases._load_json_fixture(test.get("path"))
            requests_mock.get(test.get("want_release_url"), json=response)
            result = _get_data_from_api(test.get("want_release_url"))
            got = _get_asset_download_url_by_pattern(result, ".*linux")
            assert got == test.get("want_download_url")

    def test_requests_mock(self, requests_mock: requests_mock.mocker.Mocker):
        response = {}
        requests_mock.get('http://aurl.com', json=response)
        result = _get_data_from_api('http://aurl.com')
        assert result == response

    def test_integration(self, requests_mock: requests_mock.mocker.Mocker):
        for test in TestReleases._get_test_table():
            response = TestReleases._load_json_fixture(test.get("path"))
            requests_mock.get(test.get("want_release_url"), json=response)
            result = _get_data_from_api(test.get("want_release_url"))
            got = _get_asset_download_url_by_pattern(result, ".*linux")

            tag, release_url = get_tag_and_download_url(test.get("repo_url"), ".*linux")

            assert release_url == test.get("want_download_url")
            assert tag == test.get("tag")

    def test_integration_main(self, requests_mock: requests_mock.mocker.Mocker, capsys):
        for test in TestReleases._get_test_table():
            response = TestReleases._load_json_fixture(test.get("path"))
            requests_mock.get(test.get("want_release_url"), json=response)
            args = Namespace(url=test.get("repo_url"), pattern=".*linux")
            main(args)
            out, err = capsys.readouterr()
            assert """::set-output name=release_url::{}
::set-output name=release_tag::{}
""".format(test.get("want_download_url"), test.get("tag")) == out
            assert "" == err

    @staticmethod
    def _get_test_table():
        return [

            {"path": "tests/fixtures/releases-wget-unzip.json",
             "repo_url": "https://github.com/schmiddim/action-wget-unzip",
             "want_release_url": "https://api.github.com/repos/schmiddim/action-wget-unzip/releases/latest",
             "want_download_url": "",
             "tag": "v2",
             "assets": 0

             },
            {
                "repo_url": "https://github.com/hpool-dev/chia-miner/",
                "want_release_url": "https://api.github.com/repos/hpool-dev/chia-miner/releases/latest",
                "want_download_url": "https://github.com/hpool-dev/chia-miner/releases/download/1.5.6/HPool-Miner-chia-og-v1.5.6-1-linux.zip",
                "path": "tests/fixtures/releases-chia-miner.json",
                "tag": "1.5.6",
                "assets": 4
            }
        ]

    @staticmethod
    def _load_json_fixture(path):
        with open(path) as file:
            return json.load(file)
