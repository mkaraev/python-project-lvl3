import logging

LEVELS = {
    'info': 'INFO',
    'debug': 'DEBUG'
}


def setup(log_level):
    logging.basicConfig(
        format='%(asctime)s - %(levelname)s - %(message)s',
        level=logging.getLevelName(LEVELS[log_level]),
    )
