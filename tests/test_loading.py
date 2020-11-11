import os
import tempfile

import requests_mock

from page_loader import loading


def read(file_path):
    with open(file_path, "rb") as f:
        result = f.read()
    return result


page = read("./tests/fixtures/page.html")
css_file = read("./tests/fixtures/styles.css")
photo = read("./tests/fixtures/photo.jpg")


def test_loading():
    with requests_mock.Mocker() as mock:
        url = "http://page.com"
        mock.get(url, content=page)
        mock.get(f"{url}/assets/styles.css", content=css_file)
        mock.get(f"{url}/assets/photo.jpg", content=photo)

        with tempfile.TemporaryDirectory() as temp_dir:
            loading.load(url, temp_dir)
            assert os.path.exists(os.path.join(temp_dir, "page-com.html"))
            assert os.path.exists(os.path.join(temp_dir, "page-com_files/assets-photo.jpg"))
            assert os.path.exists(os.path.join(temp_dir, "page-com_files/assets-styles.css"))
