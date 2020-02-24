import json

from ..bitcoin_api import Bitcoin


def test_parse_price_data():
    path = './utils/tests/sample_data/bitcoin-api.json'
    with open(path, 'r') as fp:
        data = json.load(fp)
        api = Bitcoin()
        price = api._parse_bitcoin_price(data=data, currency='EUR')
        assert(str(price) == '8886.61')