import logging
from urllib.parse import urlsplit

import requests

from page_loader.errors import KnownError

log = logging.getLogger()


def get(url):
    try:
        res = requests.get(url)
        res.raise_for_status()
    except requests.HTTPError as error:
        log.exception(
            str(error.args),
            exc_info=log.getEffectiveLevel() == logging.DEBUG,
        )
        raise KnownError(error)
    return res


def site_url(url):
    return "://".join(urlsplit(url)[0:2])
