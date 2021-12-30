import argparse
import requests as r
from modules.releases import *

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--url', dest='url', help="url to github repo", required=True)
    parser.add_argument('--pattern', dest='pattern', help="pattern for download url", required=False)
    parser.add_argument('--mode',
                        dest='mode',
                        help="get latest <asset_url> || get latest <release_tag>",
                        required=True,
                        choices=["asset_url", "release_tag"]
                        )

    args = parser.parse_args()
    api_url = get_api_url_for_repo(args.url)
    data = r.get(api_url).json()

    if args.mode == "asset_url":
        if args.pattern is None:
            print("--pattern must be passed when mode is asset_url")
            exit(1)

        print(get_asset_download_url_by_pattern(data, args.pattern))
    if args.mode == "release_tag":
        print(get_latest_tag(data))
