import logging
from urllib.parse import urlsplit

import requests

log = logging.getLogger()


def get(url):
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


def site_url(url):
    return "://".join(urlsplit(url)[0:2])
