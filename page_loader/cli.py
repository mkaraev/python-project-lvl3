import argparse

from page_loader import logging


def get_parser():
    parser = argparse.ArgumentParser(description="Page loader")
    parser.add_argument("url", type=str)
    parser.add_argument(
        "-o",
        "--output",
        type=str,
        help="set output directory",
    )
    parser.add_argument(
        "-l",
        "--log-level",
        choices=logging.LEVELS,
        default=logging.INFO,
        help="set log level",
    )
    return parser