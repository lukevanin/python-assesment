from typing import List

from bs4 import BeautifulSoup


class Parser:

    def __init__(self, html: str):
        self.soup = BeautifulSoup(markup=html, features='html.parser')

    def title(self) -> str:
        title = self.soup.title
        return title.string if title else ''

    def images(self) -> List[str]:
        return []

    def stylesheets(self) -> int:
        return 0
    