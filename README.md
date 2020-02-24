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