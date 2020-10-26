import logging
import os
from urllib.parse import urlsplit

import requests

log = logging.getLogger(__name__)


def get_url(url):
    try:
        res = requests.get(url)
        res.raise_for_status()
    except requests.HTTPError as err:
        log.exception(
            str(err.args),
            exc_info=log.getEffectiveLevel() == logging.DEBUG,
        )
        raise
    return res


def build_site_url(url):
    return "://".join(urlsplit(url)[0:2])


def create_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)


def save(path, data, mode="w"):
    try:
        with open(path, mode) as f:
            f.write(data)
    except PermissionError:
        log.exception(
            "Permission denied",
            exc_info=log.getEffectiveLevel() == logging.DEBUG,
        )
        raise
