from typing import Dict

from urllib.parse import urlparse

import requests

from .parser import Parser


class Scraper:

    def __init__(self, url: str):
        self.url = url
        # Parse the URL into its constituents (scheme, domain name, path, query, fragment).
        # urlparse will raise a ValueError if the input string cannot be parsed
        # https://docs.python.org/3/library/urllib.parse.html#urllib.parse.urlparse
        self.components = urlparse(url)

        # Verify that the URL has a scheme:
        if not self.components.scheme:
            raise ValueError('Expected protocol / scheme in URL')

        # Verify that the URL has a domain:
        # if not self.components.netloc:
        #     raise ValueError('Expected domain name or address in URL')


    def scrape(self, dry_run: bool = False) -> dict:
        if dry_run:
            title = ''
            image_urls = []
            stylesheets = 0
        else:
            # TODO: Errors are not handled here. Program will simply crash if there is a problem.
            if self.components.scheme == 'file':
                with open(self.components.path, 'r') as fp:
                    html = fp.read()
            else:
                html = requests.get(self.url).text
            parser = Parser(html=html)
            title = parser.title()
            image_urls = parser.images()
            stylesheets = parser.stylesheets()
        return {
            'domain_name': self.components.netloc,
            'protocol': self.components.scheme,
            'title': title,
            'image': image_urls,
            'stylesheets': stylesheets,
        }
