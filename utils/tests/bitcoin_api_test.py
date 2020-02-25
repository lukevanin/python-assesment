import json
import pytest

from ..bitcoin_api import Bitcoin


def test_parse_price_data():
    path = './utils/tests/sample_data/bitcoin-api.json'
    with open(path, 'r') as fp:
        data = json.load(fp)
        api = Bitcoin()
        price = api._parse_bitcoin_price(data=data, currency='EUR')
        assert(str(price) == '8886.61')


def test_parse_invalid_currency_price_data():
    path = './utils/tests/sample_data/bitcoin-api.json'
    with open(path, 'r') as fp:
        data = json.load(fp)
        api = Bitcoin()
        with pytest.raises(ValueError):
            api._parse_bitcoin_price(data=data, currency='ZAR')


def test_get_price():
    api = Bitcoin()
    price = api.get_bitcoin_price(currency='USD')
    assert(str(price) != '')