import logging
import os
from collections import namedtuple

from progress.bar import IncrementalBar

from page_loader import fs, paths, urls
from page_loader.logging import debug_logger

LOCAL_RESOURCES = {
    "link": "href",
    "script": "src",
    "img": "src",
}

Resource = namedtuple("Resource", "old_value, new_value")

log = logging.getLogger()


@debug_logger
def download(resources, base_url, resources_dir_name):
    log.info("Saving local resources ...")
    fs.create_directory(resources_dir_name)
    total_items = len(resources)
    bar_width = len(resources)

    with IncrementalBar("Downloading:", max=bar_width) as bar:
        bar.suffix = "%(percent).1f%% (eta: %(eta)s)"
        filled_bar = 0
        processed_percentage = 0

        for resource in resources:
            url = f"{base_url}{resource.old_value}"
            path = os.path.join(resources_dir_name, resource.new_value)
            fs.save(path, urls.get(url).content, "wb")

            processed_percentage += 1 / total_items
            if processed_percentage >= filled_bar / bar_width:
                bar.next()
                filled_bar += 1


def find(soup, path):
    resources = []
    for tag, attr in LOCAL_RESOURCES.items():
        resources.extend(_find_resources_with_tag(tag, attr, soup, path))
    return soup, resources


def _find_resources_with_tag(tag, attr, soup, path):
    resources = []
    for item in soup.find_all(tag):
        attr_val = item.get(attr)
        if _is_local(attr_val):
            base, ext = os.path.splitext(attr_val)
            if ext != "":
                new_attr_val = paths.resource(attr_val)
                resources.append(Resource(attr_val, new_attr_val))
                item[attr] = os.path.join(
                    path,
                    new_attr_val,
                )
    return resources


def _is_local(attr_value):
    return attr_value is not None and attr_value.startswith("/")
