from ..exchange_api import CurrencyExchange


def test_parse_conversion_rate():
    exchange = CurrencyExchange()
    path = './utils/tests/sample_data/exr-d-gbp-eur-20200224.json'
    with open(path, 'r') as fp:
        data = fp.read()
        rate = exchange._parse_exchange_rate(data)
        assert(str(rate) == '0.83833')