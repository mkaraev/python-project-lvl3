import pytest

from pathlib import PosixPath

from bs4 import BeautifulSoup

from page_loader import resources
from page_loader.resources import Resource

from tests.fixtures import simple_html, html_with_resources

testcases = [
    (simple_html, set()),
    (
        html_with_resources,
        {
            Resource(
                old_value="/styles/styles.css",
                new_value=PosixPath("styles-styles.css")
            ),
            Resource(
                old_value="/javascript/index.js",
                new_value=PosixPath("javascript-index.js"),
            ),
            Resource(
                old_value="/images/image1.img",
                new_value=PosixPath("images-image1.img")
            ),
            Resource(
                old_value="/images/image2.img",
                new_value=PosixPath("images-image2.img")
            ),
            Resource(
                old_value="/images/image3.img",
                new_value=PosixPath("images-image3.img")
            ),
        },
    ),
]


@pytest.mark.parametrize(
    "html, expected", testcases, ids=["Empty html", "HTML with resources"]
)
def test_find(html, expected):
    soup = BeautifulSoup(html, "html.parser")
    soup, resources_ = resources.find(soup, "./")
    assert set(resources_) == expected
