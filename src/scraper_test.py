import pytest

from scraper import Scraper


def test_valid_url_should_not_raise_exception():
    Scraper(url='http://example.org/')


def test_empty_url_should_raise_exception():
    with pytest.raises(ValueError):
        Scraper(url='')


def test_invalid_url_should_raise_exception():
    with pytest.raises(ValueError):
        Scraper(url='example')


def test_invalid_domain_url_should_raise_exception():
    with pytest.raises(ValueError):
        Scraper(url='https://')
