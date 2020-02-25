import datetime
import json

import pytest

from ..exchange_api import CurrencyExchange


def test_parse_conversion_rate():
    exchange = CurrencyExchange()
    path = './utils/tests/sample_data/exr-d-gbp-eur-20200224.json'
    with open(path, 'r') as fp:
        data = json.load(fp)
        rate = exchange._parse_exchange_rate(data)
        assert(str(rate) == '0.83833')


def test_exchange_rate_url():
    exchange = CurrencyExchange()
    actual = exchange._make_exchange_rate_url(currency='USD', date=datetime.date(2020, 2, 24))
    expected = 'https://sdw-wsrest.ecb.europa.eu/service/data/EXR/M.USD.EUR.SP00.A?startPeriod=2020-02-01&endPeriod=2020-02-29'
    assert(actual == expected)


def test_parse_last_modified():
    exchange = CurrencyExchange()
    headers = { 'Last-Modified': 'Mon, 24 Feb 2020 14:56:43 GMT' }
    actual = exchange._parse_last_modified(headers)
    expected = datetime.date(2020, 2, 24)
    assert(actual == expected)


def test_parse_invalid_last_modified():
    exchange = CurrencyExchange()
    headers = { 'Last-Modified': 'Gor, 37 Bar 9090 27:63:99 FEZ' }
    with pytest.raises(ValueError):
        exchange._parse_last_modified(headers)


def test_parse_no_last_modified():
    exchange = CurrencyExchange()
    headers = { 'Date': 'Mon, 24 Feb 2020 14:56:43 GMT' }
    with pytest.raises(ValueError):
        exchange._parse_last_modified(headers)


def test_get_exchange_rate():
    exchange = CurrencyExchange()
    rate = exchange.get_exchange_rate(currency='USD', date=datetime.date(2020, 2, 23))
    assert(str(rate) == '1.110036363636364')
