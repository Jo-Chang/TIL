import requests
from pprint import pprint

def get_btc_krw():
    order_currency = "BTC"
    payment_currency = "KRW"
    url = f"https://api.bithumb.com/public/ticker/\
        {order_currency}_{payment_currency}"
    
    # var1 = requests.get(url = url).json()
    # pprint(var1)     # res 구조 파악
    
    # var2 = var1["data"]
    # pprint(var2)    # data 구조 파악
   
    # prev_closing_price = var2["prev_closing_price"]
    
    # return prev_closing_price

    return requests.get(url = url).json()["data"]["prev_closing_price"]

if __name__ == "__main__":
    print(get_btc_krw())
    # get_btc_krw()