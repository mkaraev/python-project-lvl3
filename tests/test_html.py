import os

import tests.utils
from page_loader import html

FIXTURES_PATH = os.path.join(os.getcwd(), 'tests', 'fixtures')


def test_prepare():
    page_url = 'https://ru.hexlet.io/courses'
    page_html = tests.utils.read(
        os.path.join(FIXTURES_PATH, 'page.html')
    )
    expected_page_html = tests.utils.read(
        os.path.join(FIXTURES_PATH, 'expected-page.html')
    )
    prepared_html, _ = html.prepare(
        content=page_html,
        page_url=page_url,
        assets_dir='ru-hexlet-io-courses_files'
    )
    assert prepared_html == expected_page_html
