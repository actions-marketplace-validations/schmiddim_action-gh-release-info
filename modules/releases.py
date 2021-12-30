import re
import requests as r


def get_tag_and_download_url(github_repo: str, pattern: str):
    api_url = _get_api_url_for_repo(github_repo)
    data = _get_data_from_api(api_url)
    return _get_latest_tag(data), _get_asset_download_url_by_pattern(data, pattern)


def _get_api_url_for_repo(url: str):
    url = url.replace("https://github.com/", "https://api.github.com/repos/")
    if url[-1] != "/":
        url += "/"
    url += "releases/latest"
    return url


def _get_latest_tag(release: dict):
    tag = release.get('tag_name')
    return tag


def _get_data_from_api(url):
    data = r.get(url).json()
    return data


def _get_asset_download_url_by_pattern(release: dict, pattern):
    for asset in release.get("assets"):
        download_url = asset.get("browser_download_url")
        if re.match(pattern, download_url):
            return download_url
    return ""
