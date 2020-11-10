import logging
import os


def create_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)


def save(path, data, mode="w"):
    log = logging.getLogger()
    try:
        with open(path, mode) as f:
            f.write(data)
    except PermissionError:
        log.exception(
            "Permission denied",
            exc_info=log.getEffectiveLevel() == logging.DEBUG,
        )
        raise
