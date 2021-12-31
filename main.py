import argparse
from modules.releases import *


def main(args):
    tag, release_url = get_tag_and_download_url(args.url, args.pattern)

    print("::set-output name=release_url::{}".format(release_url))
    print("::set-output name=release_tag::{}".format(tag))


if __name__ == '__main__':
    """
    @todo test main on integration
    
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('--url', dest='url', help="url to github repo", required=True)
    parser.add_argument('--pattern', dest='pattern', help="pattern for download url", required=False, default=".*")
    args = parser.parse_args()

    main(args)
