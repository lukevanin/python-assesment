from utils.scraper import Scraper


class Program:
    """Prompt user to enter a URL:

    1. Verify the string entered is a valid URL, otherwise return an error message
    2. If it is a valid URL, display a dictionary with the following keys:

    a. “domain_name”: returns the domain name of the URL
    b. “protocol:” http or https
    c. “title”: the <title> of the page
    d. “image”: the URLs of all the images <img>
    e. "stylesheets": the number of stylesheets present in the html of the page"""

    def __init__(self, default_url: str = 'https://www.example.org/'):
        self.default_url = default_url

    def run(self):
        self.process()

    def process(self):
        # Prompt the user to enter a URL. Use a default URL if no URL was entered.
        print(f'Please enter a URL to scrape ({self.default_url}):')
        url = input()
        if not url:
            # A URL  was not provided. Use the default URL.
            url = self.default_url
        try:
            # Try scrape the web page and print the result.
            s = Scraper(url=url)
            r = s.scrape()
            print(r)
        except ValueError as e:
            # Cannot scrape the web page. Prompt the user to fix the entered URL.
            print(f'URL {url} is not valid. {e}')
            self.process()


program = Program()
program.run()
        
