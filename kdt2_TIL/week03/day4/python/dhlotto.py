import requests

URL = 'https://dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=1049'
response = requests.get(URL).json()
print(response)