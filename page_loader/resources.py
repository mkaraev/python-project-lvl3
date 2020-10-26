import logging
import os

from progress.bar import IncrementalBar

from page_loader.common import create_directory, get_url, save
from page_loader.names import build_resource_name

LOCAL_RESOURCES = {
    "link": "href",
    "script": "src",
    "img": "src",
}

log = logging.getLogger(__name__)


def download_resources(resources, base_url, resources_dir_name):
    log.info("Saving local resources ...")
    create_directory(resources_dir_name)
    total_items = len(resources)
    bar_width = 40

    with IncrementalBar("Downloading:", max=bar_width) as bar:
        bar.suffix = "%(percent).1f%% (eta: %(eta)s)"
        filled_bar = 0
        processed_percentage = 0

        for resource in resources:
            url = f'{base_url}{resource["old_value"]}'
            path = os.path.join(resources_dir_name, resource["new_value"])
            save(path, get_url(url).content, "wb")

            processed_percentage += 1 / total_items
            if processed_percentage >= filled_bar / bar_width:
                bar.next()
                filled_bar += 1


def find_resources(soup, path):
    resources = []
    for tag, attr in LOCAL_RESOURCES.items():
        for item in soup.find_all(tag):
            attr_val = item.get(attr)
            if attr_val is not None and attr_val.startswith("/"):
                base, ext = os.path.splitext(attr_val)
                if ext != "":
                    new_attr_val = build_resource_name(attr_val)
                    resources.append(
                        {
                            "old_value": attr_val,
                            "new_value": new_attr_val,
                        },
                    )
                    item[attr] = os.path.join(
                        path,
                        new_attr_val,
                    )
    log.info(f"Found {len(resources)} local resource(s) to save.")
    return soup, resources
