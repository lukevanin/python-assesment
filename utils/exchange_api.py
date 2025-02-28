import datetime
import json
import calendar

from decimal import Decimal
from typing import Optional

import requests


class CurrencyExchange:
    """Euro exchange rates provided by the European Central Bank. 
    See: https://sdw-wsrest.ecb.europa.eu/help/"""

    def _make_exchange_rate_url(self, currency: str, date: datetime.date) -> str:
        """Compose a URL for reteiving exchange rate data for the month for a given date, where the startPeriod is the 
        beginning of the month for the given date, and the endPeriod is the last day of the month for the given date."""
        (_, days_in_month) = calendar.monthrange(date.year, date.month)
        month_end_date = datetime.date(date.year, date.month, days_in_month)
        month_start_date = datetime.date(date.year, date.month, 1)
        start_date_string = month_start_date.strftime('%Y-%m-%d') # We could also do month_start_date.strftime('%Y-%m-01')
        end_date_string = month_end_date.strftime('%Y-%m-%d')
        query = f'https://sdw-wsrest.ecb.europa.eu/service/data/EXR/M.{currency}.EUR.SP00.A?startPeriod={start_date_string}&endPeriod={end_date_string}'
        return query

    def _parse_last_modified(self, headers: dict) -> Optional[datetime.date]:
        """Parses the date from the "Last-Modified" header value if available, or raises a ValueError otherwise.
        E.g. { 'Last-Modified': 'Sun, 06 Nov 1994 08:49:37 GMT' } -> '1994-11-06'"""
        # TODO: Get header ignoring case.
        value = headers.get('Last-Modified')
        if not value:
            raise ValueError('Missing expected Last-Modified header')
        time = datetime.datetime.strptime(value, '%a, %d %b %Y %H:%M:%S %Z')
        if not time:
            raise ValueError(f'Unexpected format for Last-Modified header: {value}')
        return time.date()

    def _fetch_exchange_rate(self, currency: str, date: datetime.date) -> dict:
        """Fetch exchange rate for a specific currency for the given month. If currency data is not available for the 
        date, earlier data will be returned intead.
        Returns an SDMX data dict.
        See: https://sdmx.org/wp-content/uploads/SDMX_2-1-1-SECTION_07_WebServicesGuidelines_2013-04.pdf"""
        url = self._make_exchange_rate_url(currency=currency, date=date)
        headers = { 'Accept': 'application/vnd.sdmx.data+json;version=1.0.0-wd' }
        response = requests.get(url, headers=headers)
        if len(response.text) == 0:
            # API has not returned a response. 
            # Try parse the date from Last-Modified date, and re-issue the request.
            # Raise an exception if the Last-Modified header is not available.
            last_modified_date = self._parse_last_modified(response.headers)
            if last_modified_date == date:
                # We already queried the last modified date. Avoid infinitely retrying the request. 
                # TODO: Handle indirect circular reference, where two dates redirect to each other.
                # None of these conditions should ever happen if the API is orking correctly, but we handle them anyway.
                # TODO: Raise an exception instead of crashing.
                print(f'Recursive reference: {date} redirects to {last_modified_date}')
                exit(1) 
            return self._fetch_exchange_rate(currency=currency, date=last_modified_date)
        return response.json()

    def _parse_exchange_rate(self, data: dict) -> Optional[Decimal]:
        """Parse the daily exchange rate from a SDMX JSON structure. This is intended to provide minimal functionality 
        needed to extract data from the response payload. This will extract only the first observation metric, ignoring
        any other metrics, which is sufficient for prurpose. A production parser may want to handle multiple 
        observations, possibly returning the data as a list or aggregate.
        See: https://sdmx.org/wp-content/uploads/SDMX_2-1-1-SECTION_07_WebServicesGuidelines_2013-04.pdf"""
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
        """Retrieves the latest available monthly average Euro exchange rate for a given currency (e.g. GBP) and for a 
        given month, from the European Central Bank. 
        Note: The returned value is an average for the exchange rate over the given month, not a specific date. If the 
        monthly average exchange rate is not available (ie you're requesting the average for the current calendar 
        month), then an older exchange rate will be returned instead."""
        data = self._fetch_exchange_rate(currency=currency, date=date)
        return self._parse_exchange_rate(data)
