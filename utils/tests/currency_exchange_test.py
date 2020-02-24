import datetime

from ..exchange_api import CurrencyExchange


def test_parse_conversion_rate():
    exchange = CurrencyExchange()
    path = './utils/tests/sample_data/exr-d-gbp-eur-20200224.json'
    with open(path, 'r') as fp:
        data = fp.read()
        rate = exchange._parse_exchange_rate(data)
        assert(str(rate) == '0.83833')


def test_exchange_rate_url():
    exchange = CurrencyExchange()
    actual = exchange._make_exchange_rate_url(currency='USD', date=datetime.date(2010, 2, 24))
    expected = 'https://sdw-wsrest.ecb.europa.eu/service/data/EXR/D.USD.EUR.SP00.A?startPeriod=2010-02-24'
    assert(actual == expected)
