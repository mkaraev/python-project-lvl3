import logging
import os
from collections import namedtuple

from urllib.parse import urljoin, urlparse
from bs4 import BeautifulSoup
from progress.bar import IncrementalBar

from page_loader import storage, paths, urls
from page_loader.logging import debug_logger

LOCAL_RESOURCES = {
    "link": "href",
    "script": "src",
    "img": "src",
}


log = logging.getLogger()


@debug_logger
def download(resources, base_url, resources_dir_name):
    if not resources:
        return

    log.info("Saving local resources ...")
    storage.create_directory(resources_dir_name)
    total_items = len(resources)
    bar_width = len(resources)

    with IncrementalBar("Downloading:", max=bar_width) as bar:
        bar.suffix = "%(percent).1f%% (eta: %(eta)s)"
        filled_bar = 0
        processed_percentage = 0

        for resource in resources:
            old_path, new_path = resource
            url = f"{base_url}{old_path}"
            path = os.path.join(resources_dir_name, new_path)
            storage.save(path, urls.get(url).content, "wb")

            processed_percentage += 1 / total_items
            if processed_percentage >= filled_bar / bar_width:
                bar.next()
                filled_bar += 1


def prepare(content, path):
    soup = BeautifulSoup(content, "html.parser")
    resources = []
    for tag, attr in LOCAL_RESOURCES.items():
        for item in soup.find_all(tag):
            url = item.get(attr)
            if not url:
                continue
            _, ext = os.path.splitext(url)
            if ext:
                new_url = paths.resource(url)
                resources.append((url, new_url))
                item[attr] = os.path.join(
                    path,
                    new_url,
                )
    return str(soup.prettify(formatter="html5")), resources


def _is_local(attr_value):
    return attr_value is not None and attr_value.startswith("/")
