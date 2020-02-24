"""Prompt user to enter a URL:

1. Verify the string entered is a valid URL, otherwise return an error message
2. If it is a valid URL, display a dictionary with the following keys:

a. “domain_name”: returns the domain name of the URL
b. “protocol:” http or https
c. “title”: the <title> of the page
d. “image”: the URLs of all the images <img>
e. "stylesheets": the number of stylesheets present in the html of the page"""


class Program:

    def __init__(self, default_url: str = 'https://www.exampasdle.org/'):
        self.default_url = default_url

    def run(self):
        self.process()

    def process(self):
        print(f'Please enter a URL to scrape. ({self.default_url}):')
        url = input()
        if not url:
            url = self.default_url
        print(f'URL: {url}')
        try:
            scraper = Scraper(url=url)
            result = scraper.scrape()
            print(result)
            print('Done')
        except ValueError as e:
            print(f'URL {url} is not valid. {e}')
            self.process()


program = Program()
program.run()
        
