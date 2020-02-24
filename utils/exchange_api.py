import datetime
import json

from decimal import Decimal
from typing import Union

import requests


class CurrencyExchange:

    def _make_exchange_rate_url(self, currency: str, date: datetime.date) -> str:
        date_string = date.strftime('%Y-%m-%d')
        query = f'https://sdw-wsrest.ecb.europa.eu/service/data/EXR/D.{currency}.EUR.SP00.A?startPeriod={date_string}'
        return query

    def _fetch_exchange_rate(self, currency: str, date: datetime.date ) -> str:
        url = self._make_exchange_rate_url(currency=currency, date=date)
        response = requests.get(url, headers={ 'Accept': 'application/vnd.sdmx.data+json;version=1.0.0-wd' })
        return response.text

    def _parse_exchange_rate(self, data: Union[str, bytes]) -> Decimal:
        data = json.loads(data)
        # NOTE: Use nil coalescing operators in python 3.8
        data_sets = data.get('dataSets')
        if not data_sets:
            return None
        if not len(data_sets):
            return None
        # TODO: Get latest data set in data sets
        data_set = data_sets[0]
        series = data_set.get('series')
        if not series:
            return None
        # TODO: Get latest value in series
        initial = series.get('0:0:0:0:0')
        if not initial:
            return None
        observations = initial.get('observations')
        if not observations:
            return None
        # TODO: Get latest / max observation in sequence
        observation = observations.get('0')
        if not observation:
            return None
        if not len(observation):
            return None
        value = observation[0]
        if not value:
            return None
        output = Decimal(str(value))
        return output

    def get_exchange_rate(self, currency: str, date: datetime.date) -> Decimal:
        data = self._fetch_exchange_rate(currency=currency, date=date)
        return self._parse_exchange_rate(data)
