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


# File URL without a domain is valid. e.g. file:./utils/tests/test.html
# def test_invalid_domain_url_should_raise_exception():
#     with pytest.raises(ValueError):
#         Scraper(url='https://')


def test_result_should_include_protocol():
    s = Scraper(url='http://example.org/')
    r = s.scrape(dry_run=True)
    assert(r['protocol'] == 'http')


def test_result_should_include_domain_name():
    s = Scraper(url='http://example.org/')
    r = s.scrape(dry_run=True)
    assert(r['domain_name'] == 'example.org')


def test_scrape_local_files():
    tests = [
        {
            'url': 'file:./utils/tests/sample_data/test-synthetic.html',
            'expected': {
                'protocol': 'file',
                'domain_name': '',
                'title': 'Foo',
                'image': [
                    'https://example.org/foo.png'
                ],
                'stylesheets': 2,
            },
        },
        {
            'url': 'file:./utils/tests/sample_data/test-example-org.html',
            'expected': {
                'protocol': 'file',
                'domain_name': '',
                'title': 'Example Domain',
                'image': [],
                'stylesheets': 1,
            },
        },
        {
            'url': 'file:./utils/tests/sample_data/test-google-com.html',
            'expected': {
                'protocol': 'file',
                'domain_name': '',
                'title': 'Google',
                'image': [
                    '/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png', 
                    'data:image/gif;base64,R0lGODlhAQABAIAAAP///////yH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==', 
                    'data:image/gif;base64,R0lGODlhAQABAIAAAP///////yH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==', 
                    'data:image/gif;base64,R0lGODlhAQABAIAAAP///////yH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==',
                ],
                'stylesheets': 24,
            },
        },
    ]
    for test in tests:
        s = Scraper(url=test.get('url'))
        r = s.scrape()
        for k, v in test.get('expected').items():
            assert(r.get(k) == v)
