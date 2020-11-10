import os
import re
from pathlib import Path
from urllib.parse import urlparse


def resources_dir(path):
    return Path(path.replace(".html", "_files"))


def resource(resource):
    base, ext = os.path.splitext(resource)
    base = re.sub(r"[\W_]", "-", base.replace("/", "", 1))
    return Path(f"{base}{ext}")


def page(res):
    parsed = urlparse(res)
    scheme = parsed.scheme
    page_name = parsed.geturl().lstrip(f"{scheme}://")
    page_name = re.sub(r"[\W_]", "-", page_name)
    return Path(f"{page_name}.html")
