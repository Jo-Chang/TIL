import requests

name_list = ["gunhee", "mingi", "hyunyoung", "minji", "yuyoung"]

for name in name_list:
    URL = "https://api.nationalize.io/?name=" + name
    response = requests.get(URL).json()
    # print(response)

    print(response.get("country")[0].get("country_id"))
