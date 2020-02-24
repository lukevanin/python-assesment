from typing import Dict

from urllib.parse import urlparse

import requests

from .parser import Parser


class Scraper:
    """Parses an HTML resource at a given URL, and extracts the page title, image URLs, and number of stylesheets."""

    def __init__(self, url: str):
        self.url = url
        # Parse the URL into its constituents (scheme, domain name, path, query, fragment).
        # urlparse will raise a ValueError if the input string cannot be parsed
        # https://docs.python.org/3/library/urllib.parse.html#urllib.parse.urlparse
        self.components = urlparse(url)

        # Verify that the URL has a scheme. URLLib only validates that the URL meets the RFC specifications, but does 
        # not verify that the URL is actually usable. We need the scheme to be able to correctly handle local files
        # vs remote URLs.
        if not self.components.scheme:
            raise ValueError('Expected protocol / scheme in URL')

        # TODO: Validation & tests: Verify that the URL always has at least a domain or a path.

        # Verify that the URL has a domain:
        # if not self.components.netloc:
        #     raise ValueError('Expected domain name or address in URL')


    def scrape(self, dry_run: bool = False) -> dict:
        """Downloads and parses a web page at the given URL, and returns information about the request and contents of 
        the page.

        Errata: Note that the program will crash if the provided URL cannot be loaded, or if the contents of the URL 
        cannot be loaded.
        
        Returns a dictionary containing the following:
            `domain_name`: Domain name in the URL, if provided. If the domain name is empty, such as when a local file 
            URL is used, then domain name is an empty string.
            `protocol`: Protocol scheme prefix specified in the URL. e.g. http, https, ftp, file, etc. Always present 
            after the class is constructed.
            `title`: Title of the web page, as defined by the initial <title> tag in the page header.
            `image`: List of URLs of images (img tags) embedded in the page body. Image tags which do not have a src 
            attribute are excluded from the results.
            `stylesheets`: Number of embedded and linked stylesheets. Counts both <style> and <link type="text/css"> 
            stylesheets.
        """
        if dry_run:
            title = ''
            image_urls = []
            stylesheets = 0
        else:
            # TODO: Better error handling. Errors are not handled here. Program will simply crash if there is a problem 
            # opening the given file or URL.
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
