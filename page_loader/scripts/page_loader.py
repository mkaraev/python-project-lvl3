import sys

from page_loader import cli
from page_loader import loader
from page_loader import logging


def main():
    try:
        parser = cli.get_parser()
        args = parser.parse_args()
        print(args)
        logging.configure_logger(args.log_level)
        loader.load(args.url, args.output)
    except Exception:
        sys.exit(1)


if __name__ == "__main__":
    main()