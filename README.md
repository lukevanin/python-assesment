# INTERVIEW TEST BACK-END DEVELOPER

* Use Python 3.6+ for this exercise
* Add any external library in requirements.txt
* Please send us a way to view the code (Github, Bitbucket, etc.).
* Please do both exercises

## Exercise 1

Write a script in a file One.py - When running the script in the command line, user should be
prompted to enter a URL.

1. Verify the string entered is a valid URL, otherwise return an error message
2. If it is a valid URL, display a dictionary with the following keys:

a. “domain_name”: returns the domain name of the URL
b. “protocol:” http or https
c. “title”: the <title> of the page
d. “image”: the URLs of all the images <img>
e. "stylesheets": the number of stylesheets present in the html of the page

## Exercise 2

Write a script in a file Two.py - When running the script in the command line, user should be
shown:

1. The 15min delayed bitcoin market price in EUR
2. Monthly conversion rate (last month, dynamically generated) from EUR to GBP from
the European Central Bank
3. The price from step 1 converted to GBP (official ECB rate)

## Resources

* ECB official API: https://sdw-wsrest.ecb.europa.eu/
* Bitcoin API: https://www.blockchain.com/api/exchange_rates_api

## Usage

Requires python 3.7 or above.
Install: `pip3 install -r requirements.txt`
Test: `py.test`
Run exercise one: `python3 One.py`
Run exercise two: `python3 Two.py`

## Development notes

I used requests, beautiful soup, and pytest for this project because they were used in other projects I have worked on.

I followed a test-driven approach to developing the code. For exercise one, I created separate classes and tested the 
public methods. For exercise two I was running out of time, and tested the private methods. I think either approach can 
work. Using separate classes is perhaps better for reuse and extensibility, whereas closed classes are perhaps simpler
and easier to understand.

The most difficult part of this assesment was interacting with the exchange rate API, due to the unexpected way it
returns data. As this was only assessment, I didn't want to spend a lot of time digging through the documentation I
came across the situation where the API does not return the data for the date requested, but instead returns the the "Last-Modified" date of when the most recent data is available.
  
I'm accustomed to seeing a cache control header in these situations, so when the API returned an empty response, I was
confused about what was happening. It took some time before I realised that I would have to issue multiple requests,
depending on the response from the server. I have an "apparent" solution that seems to work, although I am not sure 
whether it is doing the right thing. My current solution is:
1. Try fetch the exchange rate date for the current month.
2. If this fails, look at the Last-Modified header in the response, and query data for that date instead.
  
Here are the steps I took to debug the problem, that led to the "solution":
* Saw the request returning a "0" for the content response.
* Tried the request in CURL from the CLI. Noticed strange behaviour where content was returned in the terminal, after 
  CURL had returned to the command prompt. 
* Tried the request in the browser, while running Charles debugging proxy to intercept the connection. Saw that the 
  initial response was empty. I also saw that an additional request /response was made after the initial response, but
  Charles was not able to show the contents (I think due to SSL).
* Tried Wireshark while making the request from CURL. I could see that the response was returned as an HTTP chunked 
  response. This was new information, not shown by Charles.
* I started to suspect that the requests library might not be handling the chunked response correctly.
* I switched to urllib3 to try get lower level control over the communication channel. That gave me the same information
  I got from the requests library.
* I then tried a raw SSL socket, and could see exactly what was being sent to and from the server. The response was 
  intact, but contained a single "0" and nothing else. This was all the data that was sent before the server closed the 
  connection.
* At this point I realised the client might have to do more work, but I was unsure what was needed. I played around with
  the API parameters, namely the startPeriod and endPeriod, until I got a usable response.

Again, I don't know if my solution is correct. I suspect that digging into the documentation will confirm this as 
correct, or provide a better alternative.

