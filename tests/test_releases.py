import json

from modules.releases import *


class TestReleases:

    def test_api_release_url(self):
        repo_url = "https://github.com/schmiddim/action-wget-unzip"
        want = "https://api.github.com/repos/schmiddim/action-wget-unzip/releases"
        got = get_api_url_for_repo(repo_url)

        assert got == want

    def test_get_tag(self):
        for test in TestReleases.get_test_table():
            data = TestReleases.load_json_fixture(test.get("path"))
            want = test.get("tag")
            got = get_latest_tag(data)
            assert got == want

    @staticmethod
    def get_test_table():
        return [

            {"path": "tests/fixtures/releases-wget-unzip.json",
             "tag": "v2"

             },
            {"path": "tests/fixtures/releases-chia-miner.json",
             "tag": "1.5.6"

             }
        ]

    @staticmethod
    def load_json_fixture(path):
        with open(path) as file:
            return json.load(file)
