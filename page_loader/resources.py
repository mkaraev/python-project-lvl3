import logging

import requests


def get(url):
    response = requests.get(url)
    response.raise_for_status()
    if response.encoding is None:
        response.encoding = 'utf-8'

    logging.info(f'Got successful response from {url}')
    return response.content
