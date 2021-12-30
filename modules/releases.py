import re


def get_api_url_for_repo(url: str):
    url = url.replace("https://github.com/", "https://api.github.com/repos/")
    if url[-1] != "/":
        url += "/"
    url += "releases/latest"
    return url


def get_latest_tag(release: dict):
    tag = release.get('tag_name')
    return tag


def get_asset_download_url_by_pattern(release: dict, pattern):
    for asset in release.get("assets"):
        download_url = asset.get("browser_download_url")
        if re.match(pattern, download_url):
            return download_url
    return ""
