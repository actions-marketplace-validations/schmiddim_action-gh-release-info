""""
- name: Checkout
uses: actions/checkout@v2
- name: Get Release version
run: echo "LATEST_ARM_RELEASE_VERSION=$(curl -sL https://api.github.com/repos/hpool-dev/chia-miner/releases/latest | jq -r '.tag_name')" >> $GITHUB_ENV
- name: Get Release Url
run: echo "LATEST_ARM_RELEASE_URL=$(curl -sL https://api.github.com/repos/hpool-dev/chia-miner/releases/latest |  jq -r '.assets|.[] |.browser_download_url' |grep linux)" >> $GITHUB_ENV
- name: output software version
run: echo $LATEST_ARM_RELEASE_URL version is  $LATEST_ARM_RELEASE_VERSION
"""
import re


def get_api_url_for_repo(url: str):
    url = url.replace("https://github.com/", "https://api.github.com/repos/")
    if url[:-1] != "/":
        url += "/"
    url += "releases"
    return url


def get_latest_tag(release: dict):
    tag = release.get('tag_name')
    return tag


def get_assets(release: dict):
    assets = release.get("assets")
    return assets


def get_asset_download_url_by_pattern(release: dict, pattern):
    for asset in get_assets(release):
        download_url = asset.get("browser_download_url")
        if re.match(pattern, download_url):
            return download_url
    pass
