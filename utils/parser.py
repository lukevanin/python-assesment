from typing import List

from bs4 import BeautifulSoup


class Parser:
    """Parse an HTML file and extract the title, image URLs and stylesheets."""

    def __init__(self, html: str):
        self.soup = BeautifulSoup(markup=html, features='html.parser')

    def title(self) -> str:
        """Returns the text contents from the first <title> tag in the HTML document."""
        title = self.soup.title
        return title.string if title else ''

    def images(self) -> List[str]:
        """Returns a list of URLs from the rc attribute of <img> tags in the HTML document.""" 
        images = self.soup.find_all(name='img')
        return [image.get('src') for image in images if image.get('src') is not None]

    def stylesheets(self) -> int:
        """Returns the number of stylesheets in the HTML document. The count includes all <style> tags, and 
        <link type="text/css"> tags, according to the HTML 4 specification: 
        https://www.w3.org/TR/html4/present/styles.html"""
        count = len(self.soup.find_all(name='style'))
        link_tags = self.soup.find_all(name='link')
        for tag in link_tags:
            if tag.get('type') == 'text/css':
                count += 1
        return count
    