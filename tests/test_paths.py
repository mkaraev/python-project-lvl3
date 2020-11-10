import pytest
from pathlib import PosixPath
from page_loader import paths


@pytest.mark.parametrize(
    "path, expected",
    [
        ("test.html", PosixPath("test_files")),
        ("abc-abc.html", PosixPath("abc-abc_files")),
    ],
)
def test_resource_dir(path, expected):
    assert paths.resources_dir(path) == expected


@pytest.mark.parametrize(
    "resource, expected",
    [
        ("/assets/application.css", PosixPath("assets-application.css")),
        ("/assets/application.img", PosixPath("assets-application.img")),
    ],
)
def test_resource(resource, expected):
    assert paths.resource(resource) == expected


@pytest.mark.parametrize(
    "page, expected",
    [
        ("https://hexlet.io/courses", PosixPath("hexlet-io-courses.html")),
        ("https://hexlet.io/my", PosixPath("hexlet-io-my.html")),
    ],
)
def test_page(page, expected):
    assert paths.page(page) == expected
