from http import HTTPStatus
import pytest
import os

from requests.exceptions import RequestException

import tests.utils
from page_loader import download

FIXTURES_PATH = os.path.join(os.getcwd(), 'tests', 'fixtures')


def test_download_page_with_some_unavailable_resources(requests_mock, tmpdir):
    page_html = '''
        <html>
            <body>
                <img src="unavailable.png">
                <img src="available.png">
            <body>
        </html>
    '''
    page_url = 'http://test.com'
    requests_mock.get(page_url, text=page_html)
    requests_mock.get(page_url + '/unavailable.png',
                      status_code=HTTPStatus.NOT_FOUND)
    requests_mock.get(page_url + '/available.png', content=b'\xFF')

    download(page_url, str(tmpdir))

    resources_dir_path = tmpdir / 'test-com_files'
    assert os.path.isfile(tmpdir / 'test-com.html')
    assert not os.path.isfile(resources_dir_path / 'test-com-unavailable.png')
    assert os.path.isfile(resources_dir_path / 'test-com-available.png')


def test_download_page_without_resources(requests_mock, tmpdir):
    page_url = 'http://test.com'
    requests_mock.get(page_url, text='<html></html>')

    download(page_url, str(tmpdir))

    resources_dir_path = tmpdir / 'test-com_files'
    assert os.path.isfile(tmpdir / 'test-com.html')
    assert not os.path.isdir(resources_dir_path)


def test_download_unavailable_page(requests_mock, tmpdir):
    page_url = 'http://test.com'
    requests_mock.get(page_url, status_code=HTTPStatus.NOT_FOUND)

    with pytest.raises(RequestException):
        download(page_url, str(tmpdir))


def test_download_with_non_existing_output_dir(requests_mock):
    page_url = 'http://test.com'
    requests_mock.get(page_url, text='<html></html>')

    with pytest.raises(OSError):
        download(page_url, 'non/existing/dir/path')


def test_download_page_with_resources(requests_mock, tmpdir):
    page_html = tests.utils.read(
        os.path.join(FIXTURES_PATH, 'page.html')
    )
    application_css_content = tests.utils.read(
        os.path.join(FIXTURES_PATH, 'assets/application.css')
    )
    application_js_content = tests.utils.read(
        os.path.join(FIXTURES_PATH, 'assets/application.js')
    )
    runtime_js_content = tests.utils.read(
        os.path.join(FIXTURES_PATH, 'assets/runtime.js')
    )
    python_png_binary = tests.utils.read(
        os.path.join(FIXTURES_PATH, 'assets/python.png'), mode='rb'
    )
    page_url = 'https://ru.hexlet.io/courses'

    mocks = [
        (
            page_url,
            page_html,
        ),
        (
            'https://ru.hexlet.io/assets/application.css',
            application_css_content,
        ),
        (
            'https://ru.hexlet.io/assets/application.js',
            application_js_content,
        ),
        (
            'https://ru.hexlet.io/packs/js/runtime.js',
            runtime_js_content,
        ),
        (
            'https://ru.hexlet.io/assets/professions/python.png',
            python_png_binary,
        ),
    ]
    for url, content in mocks:
        if isinstance(content, bytes):
            requests_mock.get(url, content=content)
        else:
            requests_mock.get(url, text=content)

    page_file_path = tmpdir / 'ru-hexlet-io-courses.html'

    assert download(page_url, str(tmpdir)) == page_file_path
    assert tests.utils.read(page_file_path) == tests.utils.read(
        os.path.join(FIXTURES_PATH, 'expected-page.html')
    )

    resources = [
        ('ru-hexlet-io-assets-application.css', application_css_content),
        ('ru-hexlet-io-assets-application.js', application_js_content),
        ('ru-hexlet-io-packs-js-runtime.js', runtime_js_content),
        ('ru-hexlet-io-assets-professions-python.png', python_png_binary),
    ]
    resources_dir_path = tmpdir / 'ru-hexlet-io-courses_files'
    for name, content in resources:
        resource_path = resources_dir_path / name
        read_mode = 'rb' if isinstance(content, bytes) else 'r'
        assert tests.utils.read(resource_path, mode=read_mode) == content
