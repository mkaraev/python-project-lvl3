import os
import re
from pathlib import Path
from urllib.parse import urlparse


def resources_dir(path_to_page):
    return path_to_page.replace(".html", "_files")


def resource(resource):
    base, extension = os.path.splitext(resource)
    base = re.sub(r"[\W_]", "-", base.replace("/", "", 1))
    return f"{base}{extension}"


def page(url):
    parsed = urlparse(url)
    scheme = parsed.scheme
    page_name = parsed.geturl()[len(f"{scheme}://"):]
    page_name = re.sub(r"[\W_]", "-", page_name)
    return f"{page_name}.html"
