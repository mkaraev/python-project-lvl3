import logging
import sys

import page_loader.logging
from page_loader import cli, loading


def main():
    parser = cli.get_parser()
    args = parser.parse_args()
    page_loader.logging.setup(args.log_level)
    try:
        html_page_path = loading.download(args.url, args.output)
        print(f"Done. You can open saved page from: {html_page_path}")
    except Exception as error:
        logging.error(f"Download failed: {error}")
        sys.exit(1)


if __name__ == "__main__":
    main()
