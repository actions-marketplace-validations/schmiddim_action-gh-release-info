import json

from modules.releases import *


class TestReleases:

    def test_api_release_url(self):

        test_table = [

            {
                "repo_url": "https://github.com/schmiddim/action-wget-unzip",
                "want": "https://api.github.com/repos/schmiddim/action-wget-unzip/releases/latest"
            },
            {
                "repo_url": "https://github.com/hpool-dev/chia-miner/",
                "want": "https://api.github.com/repos/hpool-dev/chia-miner/releases/latest"
            },
        ]
        for test in test_table:
            got = get_api_url_for_repo(test.get("repo_url"))
            assert got == test.get("want")

    def test_get_tag(self):
        for test in TestReleases.get_test_table():
            data = TestReleases.load_json_fixture(test.get("path"))
            want = test.get("tag")
            got = get_latest_tag(data)
            assert got == want

    def test_assets(self):
        for test in TestReleases.get_test_table():
            data = TestReleases.load_json_fixture(test.get("path"))
            want = test.get("assets")
            got = get_assets(data)
            assert len(got) == want

        data = TestReleases.load_json_fixture("tests/fixtures/releases-chia-miner.json")
        want = "https://github.com/hpool-dev/chia-miner/releases/download/1.5.6/HPool-Miner-chia-og-v1.5.6-1-linux.zip"
        got = get_asset_download_url_by_pattern(data, ".*linux")

        assert got == want

    @staticmethod
    def get_test_table():
        return [

            {"path": "tests/fixtures/releases-wget-unzip.json",
             "tag": "v2",
             "assets": 0
             },
            {"path": "tests/fixtures/releases-chia-miner.json",
             "tag": "1.5.6",
             "assets": 4
             }
        ]

    @staticmethod
    def load_json_fixture(path):
        with open(path) as file:
            return json.load(file)
