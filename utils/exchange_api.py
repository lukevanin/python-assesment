import json

from typing import Union

from decimal import Decimal


class CurrencyExchange:

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

    def exchange_rate(currency: str) -> Decimal:
        # TODO: Get current date and convert to YYYY-MM-DD format
        # TODO: Fetch exchange rate data from the API
        # TODO: Parse and extract current exchange rate
        # TODO: Convert 
        pass