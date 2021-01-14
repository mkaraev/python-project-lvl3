import os
import pytest

from page_loader import resources
from page_loader import storage


def get_fixture_path(file_name):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_dir, 'fixtures', file_name)


@pytest.mark.parametrize(
    "html, expected",
    [
        ("simple.html", set()),
        ("with_resources.html", {
            ("/styles/styles.css", "styles-styles.css"),
            ("/javascript/index.js", "javascript-index.js"),
            ("/images/image1.img", "images-image1.img"),
            ("/images/image2.img", "images-image2.img"),
            ("/images/image3.img", "images-image3.img"),
        })
    ],
    ids=["Empty html", "HTML with resources"]
)
def test_find(html, expected):
    html = storage.read(get_fixture_path(html))
    html, resources_ = resources.prepare(html, "./")
    assert set(resources_) == expected
