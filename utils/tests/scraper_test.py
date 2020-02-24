import pytest

from ..scraper import Scraper


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


def test_result_should_include_protocol():
    s = Scraper(url='http://example.org/')
    r = s.scrape(dry_run=True)
    assert(r['protocol'] == 'http')


def test_result_should_include_domain_name():
    s = Scraper(url='http://example.org/')
    r = s.scrape(dry_run=True)
    assert(r['domain_name'] == 'example.org')