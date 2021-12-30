import argparse
import requests as r
from modules.releases import *

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--url', dest='url', help="url to github repo", required=True)
    parser.add_argument('--pattern', dest='pattern', help="pattern for download url", required=False, default=".*")
    args = parser.parse_args()

    api_url = get_api_url_for_repo(args.url)
    data = r.get(api_url).json()
    url = get_asset_download_url_by_pattern(data, args.pattern)
    tag = get_latest_tag(data)
    print(f"::set-output name=release_url::{url}")
    print(f"::set-output name=release_tag::{tag}")
