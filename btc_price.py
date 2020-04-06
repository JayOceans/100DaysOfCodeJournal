# get the current BTC price

import requests

API_URL = 'https: // api.coinmarketcap.com/v1/ticker/'


def get_price():
    responce = requests.get(API_URL)
    responce_json = responce.json()
    return float(responce_json[0]['price_usd'])


get_price()
