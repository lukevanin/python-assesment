import requests


class Bitcoin:

    def ticker(self) -> dict:
        return requests.get('https://blockchain.info/ticker', headers={ 'Accept': 'application/json' })