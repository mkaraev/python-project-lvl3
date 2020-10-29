import logging
import os
from pathlib import Path

from bs4 import BeautifulSoup

from page_loader import naming
from page_loader.common import save, get_url, build_site_url
from page_loader.resources import find_resources, download_resources

log = logging.getLogger(__name__)


def load(url, output=Path(".")):
    url = url.rstrip("/")
    html_file_path = os.path.join(output, naming.build_html_file_name(url))
    resources_dir_name = naming.build_resources_directory_name(html_file_path)

    log.info(f"Saving {url} to the {output} ...")
    soup, resources = find_resources(
        BeautifulSoup(get_url(url).content, "html.parser"),
        resources_dir_name,
    )

    save(html_file_path, str(soup.prettify()))
    if resources:
        download_resources(
            resources,
            build_site_url(url),
            resources_dir_name,
        )
    log.info(f"Done. You can open saved page from: {html_file_path}")
