import requests
import pprint

URL = "https://api.bithumb.com/public/ticker/ALL_KRW"
response = requests.get(URL)
# print(response)
# print(type(response))
# print(dir(response))
# print(response.json())

# pprint.pprint(response.json())
# data = response.json()
print(response.json().get("data").get("BTC").get("closing_price"))


"""__danger__
# 웹크롤링 요청 반복으로 웹 사이트 트래픽 폭주...

while True:
    URL = "https://api.bithumb.com/public/ticker/ALL_KRW"
    response = requests.get(URL)

    print(response.json().get("data").get("BTC").get("closing_price"))
"""