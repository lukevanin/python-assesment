from typing import Dict

from urllib.parse import urlparse


class Scraper:

    def __init__(self, url: str):
        # Parse the URL into its constituents (scheme, domain name, path, query, fragment).
        # urlparse will raise a ValueError if the input string cannot be parsed
        # https://docs.python.org/3/library/urllib.parse.html#urllib.parse.urlparse
        self.components = urlparse(url)
        

    def scrape(self) -> Dict[str, any]:
        return {
            'domain_name': self.components.netloc,
            'protocol': self.components.scheme,
        }
