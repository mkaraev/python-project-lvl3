import pytest
import page_loader.url


@pytest.mark.parametrize(
    'url, file_name',
    [('https://ru.hexlet.io', 'ru-hexlet-io.html'),
     ('http://www.google.com', 'www-google-com.html'),
     ('https://test.com/file.txt', 'test-com-file.txt'),
     ('http://test.ru/a/b/c.pdf', 'test-ru-a-b-c.pdf')]
)
def test_url_to_file_name(url, file_name):
    assert page_loader.url.to_file_name(url) == file_name
