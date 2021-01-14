import logging
import os

from page_loader.errors import KnownError


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


def read(file_path, mode='r'):
    with open(file_path, mode) as f:
        return f.read()
