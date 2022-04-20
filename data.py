import config as cfg
import pprint
import requests


def getData(currency):
    url = f"https://rest.coinapi.io/v1/exchangerate/{currency}/USD"
    headers = {'X-CoinAPI-Key': cfg.x_coin_api_key}
    response = requests.get(url, headers=headers)

    return response.json()


def convert_name(cur):
    names = {
        "Bitcoin": "BTC",
        "Ethereum": "ETH",
        "Tether": "USDT",
        "BNB": "BNB",
        "XRP": "XRP",
        "Solana": "SOL",
        "Dogecoin": "DOGE",
        "Terra": "LUNA"

    }
    return names[cur]


def getCur(text):
    return text[text.find("«") + 1:text.find("»")]


def getImgName(message):
    pic = {
        "Bitcoin": "BTC.png",
        "Ethereum": "ETH.png",
        "Tether": "USDT.png",
        "BNB": "BNB.png",
        "XRP": "XRP.png",
        "Solana": "SOL.png",
        "Dogecoin": "DOGE.png",
        "Terra": "LUNA.png"


    }
    return pic[message.text]
