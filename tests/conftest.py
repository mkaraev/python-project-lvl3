import pytest

from page_loader import storage


@pytest.fixture()
def html():
    return storage.read("./tests/fixtures/page.html", mode='rb')


@pytest.fixture()
def css():
    return storage.read("./tests/fixtures/styles.css", mode='rb')


@pytest.fixture()
def photo():
    return storage.read("./tests/fixtures/photo.jpg", mode="rb")
