import logging
import os
from pathlib import Path

from bs4 import BeautifulSoup

from page_loader import fs, paths, resources, urls
from page_loader.logging import debug_logger


@debug_logger
def load(url, output=Path(".")):
    log = logging.getLogger()

    url = url.rstrip("/")
    page = os.path.join(output, paths.page(url))
    resources_dir = paths.resources_dir(page)

    log.info(f"Saving {url} to the {output} ...")
    page_content = urls.get(url).content
    soup, resources_ = resources.find(
        BeautifulSoup(page_content, "html.parser"),
        resources_dir,
    )
    log.info(f"Found {len(resources_)} local resource(s) to save.")
    fs.save(page, str(soup.prettify()))

    if resources_:
        resources.download(
            resources_,
            urls.site_url(url),
            resources_dir,
        )
    log.info(f"Done. You can open saved page from: {page}")
