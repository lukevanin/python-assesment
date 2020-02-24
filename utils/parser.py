from bs4 import BeautifulSoup


class Parser:
    def parse(self, html: str) -> dict:
        soup = BeautifulSoup(markup=html, features='html.parser')
        title = soup.title
        return {
            'title': title.string if title else '',
            'image_urls': [],
            'stylesheet_count': 0,
        }