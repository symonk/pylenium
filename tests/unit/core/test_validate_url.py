from pylenium import validate_url
from pytest import raises
from pytest import UsageError


def test_url_valid():
    url = "https://www.google.com"
    assert validate_url(url) == url


def test_invalid_url():
    with raises(UsageError):
        assert validate_url("google")
