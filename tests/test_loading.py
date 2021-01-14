import os
import tempfile

import requests_mock

from page_loader import loading, storage


def test_loading(html, css, photo):
    with requests_mock.Mocker() as mock:
        url = "http://page.com"
        mock.get(url, content=html)
        mock.get(f"{url}/assets/styles.css", content=css)
        mock.get(f"{url}/assets/photo.jpg", content=photo)

        with tempfile.TemporaryDirectory() as temp_dir:
            loading.load(url, temp_dir)
            assert os.path.exists(os.path.join(temp_dir, "page-com.html"))
            assert os.path.exists(
                os.path.join(temp_dir, "page-com_files/assets-photo.jpg")
            )
            assert os.path.exists(
                os.path.join(temp_dir, "page-com_files/assets-styles.css")
            )
