import os
from tempfile import TemporaryDirectory

from page_loader.loader import load


def read_file(path):
    with open(path) as f:
        return f.read()


def test_load():
    with TemporaryDirectory() as tmpdir:
        load('http://example.com', tmpdir)
        actual = read_file(os.path.join(tmpdir, 'example-com.html'))
        expected = read_file('./tests/fixtures/example-com.html')
        assert actual == expected


def test_has_local_resources():
    with TemporaryDirectory() as tmpdir:
        load('https://clojure.org', tmpdir)
        expected = os.path.join(
            tmpdir,
            'clojure-org_files',
        )
        assert len(os.listdir(os.path.join(expected))) != 0

