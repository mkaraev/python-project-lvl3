import logging
import os

from progress.bar import IncrementalBar
from requests.exceptions import RequestException

import page_loader.url
from page_loader import storage, resources, html


def download(url, output="."):
    url = url.rstrip("/")
    assets_dir = page_loader.url.to_dir_name(url)
    assets_path = os.path.join(output, assets_dir)

    html_page_path = os.path.join(output, page_loader.url.to_file_name(url))

    logging.info(f"Saving {url} to the {output} ...")

    page_content = resources.get(url)
    page, assets = html.prepare(page_content, url, assets_dir)
    logging.info('Saving html file: %s', html_page_path)
    storage.save(html_page_path, page)
    download_assets(assets, assets_path)
    return html_page_path


def download_assets(assets, assets_path):
    if not assets:
        return

    if not os.path.exists(assets_path):
        logging.info('Create directory for assets: %s', assets_path)
        os.mkdir(assets_path)

    bar_width = len(assets)

    with IncrementalBar("Downloading:", max=bar_width) as bar:
        bar.suffix = "%(percent).1f%% (eta: %(eta)s)"

        for url, file_name in assets:
            try:
                asset_content = resources.get(url)
                storage.save(os.path.join(assets_path, file_name),
                             asset_content)
                bar.next()

            except (RequestException, OSError) as e:
                cause_info = (e.__class__, e, e.__traceback__)
                logging.debug(str(e), exc_info=cause_info)
                logging.warning(
                    f"Page resource {url} wasn't downloaded"
                )
