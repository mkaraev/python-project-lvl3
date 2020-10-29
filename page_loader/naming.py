import os
import re
from pathlib import Path
from urllib.parse import urlparse

from page_loader.logging import debug_logger


@debug_logger
def build_resources_directory_name(path):
    return Path(path.replace(".html", "_files"))


@debug_logger
def build_resource_name(resource):
    base, ext = os.path.splitext(resource)
    base = re.sub(r"[\W_]", "-", base.replace("/", "", 1))
    return Path(f"{base}{ext}")


@debug_logger
def build_html_file_name(res):
    parsed = urlparse(res)
    scheme = parsed.scheme
    page_name = parsed.geturl().lstrip(f"{scheme}://")
    page_name = re.sub(r"[\W_]", "-", page_name)
    return Path(f"{page_name}.html")
