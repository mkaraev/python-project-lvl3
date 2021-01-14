import sys

import page_loader.cli
import page_loader.errors
from page_loader import cli
from page_loader import loading
from page_loader import logging


def main():
    parser = cli.get_parser()
    args = parser.parse_args()
    logging.configure(args.log_level)

    try:
        loading.load(args.url, args.output)
    except page_loader.errors.KnownError:
        sys.exit(1)


if __name__ == "__main__":
    main()
