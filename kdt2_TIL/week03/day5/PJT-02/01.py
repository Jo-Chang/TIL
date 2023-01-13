import requests
from dotenv import dotenv_values
from pprint import pprint

def popular_count():
    
    # 여기에 코드를 작성합니다.  
    BASE_URL = "https://api.themoviedb.org/3"
    path = "/movie/popular"
    my_params = {
        "api_key": dotenv_values("../python/movie.env").get("API_KEY"),
        # "name": "kcj"
    }
    
    "https://api.themoviedb.org/3/movie/popular?api_key=6fecd123458567&name=kcj"
    
    # get("https://api.themoviedb.org/3/movie/popular", params=my_params)
    # BASE_URL+path == "https://api.themoviedb.org/3/movie/popular"
    
    res = requests.get(BASE_URL+path, params=my_params).json()
    # pprint(res)
    # pprint(res.get("results"))
    
    return len(res.get("results"))
    

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20
