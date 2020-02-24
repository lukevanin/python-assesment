"""Write a script in a file Two.py - When running the script in the command line, user should be
shown:

1. The 15min delayed bitcoin market price in EUR
2. Monthly conversion rate (last month, dynamically generated) from EUR to GBP from
the European Central Bank
3. The price from step 1 converted to GBP (official ECB rate)

## Resources

* ECB official API: https://sdw-wsrest.ecb.europa.eu/
* Bitcoin API: https://www.blockchain.com/api/exchange_rates_api"""
from datetime import date

from utils.bitcoin_api import Bitcoin
from utils.exchange_api import CurrencyExchange


class Program:

    def run(self):
        bitcoin_api = Bitcoin()
        price_eur = bitcoin_api.get_bitcoin_price(currency='EUR')
        print(f'BITCOIN PRICE EUR (15 min delayed): {price_eur} EUR')
        exchange_api = CurrencyExchange()
        eur_gbp_rate = exchange_api.get_exchange_rate(currency='GBP', date=date.today())
        print(f'EUR / GBP EXCHANGE RATE: 1 EUR = {eur_gbp_rate} GBP')
        price_gbp = price_eur * eur_gbp_rate
        print(f'BITCOIN PRICE GBP: {price_gbp} GBP')

program = Program()
program.run()