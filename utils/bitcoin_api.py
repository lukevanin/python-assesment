from decimal import Decimal

import requests


class Bitcoin:

    def _parse_bitcoin_price(self, data: dict, currency: str) -> Decimal:
        """Returns the '15 minute' Bitcoin price for a given currency (e.g. USD) from a Bitcoin ticket API 
        response payload. 
        Raises a value error if no 15m price data is available for the given currency code.
        e.g. { "USD" : {"15m" : 9640.53, "symbol" : "$"} } -> '9640.53'"""
        info = data.get(currency)
        if not info:
            raise ValueError(f'No data for currency {currency}')
        value = info.get('15m')
        if not value:
            raise ValueError(f'No 15-minute data for currency {currency}')
        return Decimal(str(value))
 
    def _fetch_bitcoin_price_data(self) -> dict:
        """Returns Bitcoin price for multiple currencies from the blockchain ticker API."""
        response = requests.get('https://blockchain.info/ticker', headers={ 'Accept': 'application/json' })
        return response.json()

    def get_bitcoin_price(self, currency: str) -> Decimal:
        data = self._fetch_bitcoin_price_data()
        return self._parse_bitcoin_price(data=data, currency=currency)
