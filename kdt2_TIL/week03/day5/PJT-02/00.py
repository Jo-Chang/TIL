import requests
from pprint import pprint

def get_btc_krw():
    order_currency = "BTC"
    payment_currency = "KRW"
    url = f"https://api.bithumb.com/public/ticker/\
        {order_currency}_{payment_currency}"
    
    res = requests.get(url = url).json()
    pprint(res)     # res 구조 파악
    
    data = res["data"]
    pprint(data)    # data 구조 파악
   
    prev_closing_price = data["prev_closing_price"]
    
    return prev_closing_price

if __name__ == "__main__":
    # print(get_btc_krw())
    get_btc_krw()