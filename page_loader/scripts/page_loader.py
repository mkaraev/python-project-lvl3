import sys

from page_loader import cli
from page_loader import loading
from page_loader import logging


def main():
    try:
        parser = cli.get_parser()
        args = parser.parse_args()
        logging.configure_logger(args.log_level)
        loading.load(args.url, args.output)
    except logging.KnownError:
        sys.exit(1)


if __name__ == "__main__":
    main()
