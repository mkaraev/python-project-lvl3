import pytest
from page_loader import paths


@pytest.mark.parametrize(
    "path, expected",
    [
        ("")
    ]
)
def test_resource_dir(path, expected):
    paths.resources_dir('')
