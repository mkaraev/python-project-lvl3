import os
import re
from urllib.parse import urlparse

PATH_CHARS = re.compile(r'[^A-Za-z0-9]+')


def _url_to_name_and_ext(url):
    parsed_url = urlparse(url)
    (path, ext) = os.path.splitext(parsed_url.path)
    name = re.sub(PATH_CHARS, '-', parsed_url.netloc + path)
    return name, ext


def to_dir_name(url):
    name, ext = _url_to_name_and_ext(url)
    return '{}_files'.format(name)


def to_file_name(url, ext='.html'):
    name, file_ext = _url_to_name_and_ext(url)
    if file_ext:
        ext = file_ext
    return re.sub('^-', '', name) + ext


def is_local(url, root_url):
    hostname = urlparse(url).hostname
    return hostname is None or hostname == urlparse(root_url).hostname


def get_root_url(url):
    result = urlparse(url)
    return result.scheme + '://' + result.hostname
