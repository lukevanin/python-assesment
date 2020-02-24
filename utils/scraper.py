from typing import Dict

from urllib.parse import urlparse


class Scraper:

    def __init__(self, url: str):
        # Parse the URL into its constituents (scheme, domain name, path, query, fragment).
        # urlparse will raise a ValueError if the input string cannot be parsed
        # https://docs.python.org/3/library/urllib.parse.html#urllib.parse.urlparse
        self.components = urlparse(url)

        # Verify that the URL has a scheme:
        if not self.components.scheme:
            raise ValueError('Expected protocol / scheme in URL')

        # Verify that the URL has a domain:
        if not self.components.netloc:
            raise ValueError('Expected domain name or address in URL')


    def scrape(self, dry_run: bool = False) -> Dict[str, any]:
        if not dry_run:
            # TODO: Fetch contents of URL
            # TODO: Parse 
            # TODO: Extract title, images, and stylesheets
            pass
        return {
            'domain_name': self.components.netloc,
            'protocol': self.components.scheme,
        }
