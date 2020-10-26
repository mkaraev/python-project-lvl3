import logging
import os
import re
from urllib.parse import urlparse

from page_loader.logging import debug_logger

log = logging.getLogger(__name__)


@debug_logger
def build_resources_directory_name(path):
    return path.replace(".html", "_files")


@debug_logger
def build_resource_name(res):
    base, ext = os.path.splitext(res)
    base = re.sub(r"[\W_]", "-", base.replace("/", "", 1))
    return f"{base}{ext}"


@debug_logger
def build_html_file_name(res):
    parsed = urlparse(res)
    scheme = parsed.scheme
    page_name = parsed.geturl().lstrip(f"{scheme}://")
    page_name = re.sub(r"[\W_]", "-", page_name)
    return f"{page_name}.html"
