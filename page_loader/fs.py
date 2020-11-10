import logging
import os

from page_loader.logging import KnownError


def create_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)


def save(path, data, mode="w"):
    log = logging.getLogger()
    try:
        with open(path, mode) as f:
            f.write(data)
    except PermissionError as error:
        log.exception(
            "Permission denied",
            exc_info=log.getEffectiveLevel() == logging.DEBUG,
        )
        raise KnownError(error)
