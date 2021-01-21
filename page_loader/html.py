import os
from urllib.parse import urljoin

from bs4 import BeautifulSoup

import page_loader.url

LOCAL_RESOURCE = {
    "link": "href",
    "script": "src",
    "img": "src",
}


def prepare(content, page_url, assets_dir):
    soup = BeautifulSoup(content, "html.parser")
    tags = [*soup('script'), *soup('link'), *soup('img')]
    root_url = page_loader.url.get_root_url(page_url)
    assets = []
    for tag in tags:
        name = LOCAL_RESOURCE[tag.name]
        url = tag.get(name)
        if not (url and page_loader.url.is_local(url, root_url)):
            continue

        full_asset_url = urljoin(root_url, url)
        asset_path = page_loader.url.to_file_name(full_asset_url)
        tag[name] = os.path.join(assets_dir, asset_path)
        assets.append((full_asset_url, asset_path))

    return soup.prettify(formatter="html5"), assets
