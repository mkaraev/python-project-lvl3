import logging
import os
from pathlib import Path

from page_loader import storage, paths, resources, urls
from page_loader.logging import debug_logger


@debug_logger
def load(url, output="."):
    log = logging.getLogger()

    url = url.rstrip("/")
    page_path = os.path.join(output, paths.page(url))
    resources_dir = paths.resources_dir(page_path)

    log.info(f"Saving {url} to the {output} ...")
    page_content = urls.get(url).text
    page, resources_ = resources.prepare(
        page_content,
        resources_dir,
    )
    log.info(f"Found {len(resources_)} local resource(s) to save.")
    storage.save(page_path, page)

    resources.download(
        resources_,
        urls.site_url(url),
        resources_dir,
    )
    log.info(f"Done. You can open saved page from: {page_path}")
