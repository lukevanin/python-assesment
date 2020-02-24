from typing import List

from bs4 import BeautifulSoup


class Parser:

    def __init__(self, html: str):
        self.soup = BeautifulSoup(markup=html, features='html.parser')

    def title(self) -> str:
        title = self.soup.title
        return title.string if title else ''

    def images(self) -> List[str]:
        images = self.soup.find_all(name='img')
        return [image.get('src') for image in images if image.get('src') is not None]

    def stylesheets(self) -> int:
        """https://www.w3.org/TR/html4/present/styles.html"""
        count = len(self.soup.find_all(name='style'))
        link_tags = self.soup.find_all(name='link')
        for tag in link_tags:
            if tag.get('type') == 'text/css':
                count += 1
        return count
    