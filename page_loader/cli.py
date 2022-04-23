import argparse

import page_loader.logging


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
        '-l',
        '--log-level',
        choices=page_loader.logging.LEVELS.keys(),
        default='info',
        help='set log level',
    )
    return parser
