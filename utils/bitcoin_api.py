from decimal import Decimal

import requests


class Bitcoin:

    def _parse_bitcoin_price(self, data: dict, currency: str) -> Decimal:
        info = data.get(currency)
        if not info:
            return None
        value = info.get('15m')
        if not value:
            return None
        return Decimal(str(value))
 
    def _fetch_bitcoin_price_data(self) -> dict:
        response = requests.get('https://blockchain.info/ticker', headers={ 'Accept': 'application/json' })
        return response.json()

    def get_bitcoin_price(self, currency: str) -> Decimal:
        data = self._fetch_bitcoin_price_data()
        return self._parse_bitcoin_price(data=data, currency=currency)
