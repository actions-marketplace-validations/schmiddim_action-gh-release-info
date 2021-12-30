import json

import pytest

from modules.releases import *


class TestReleases:

    def test_api_release_url(self):
        repo_url = "https://github.com/schmiddim/action-wget-unzip"
        want = "https://api.github.com/repos/schmiddim/action-wget-unzip/releases"
        got = get_api_url_for_repo(repo_url)

        assert got == want





