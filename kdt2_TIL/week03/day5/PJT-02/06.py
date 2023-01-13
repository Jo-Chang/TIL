import requests
from pprint import pprint
import os
from dotenv import load_dotenv

def credits(title):
    pass
    # 여기에 코드를 작성합니다.
    load_dotenv("../python/movie.env", verbose=True)
    BASE_URL = "https://api.themoviedb.org/3"
    path1 = "/search/movie"
    params = {
        "api_key": os.getenv("API_KEY"),
        "language": "ko-KR",
        "query": title,
    }
    
    res1 = requests.get(BASE_URL+path1, params=params).json()
    if len(res1.get("results")) == 0:
        return None
    
    movie_id = res1.get("results")[0].get("id")
    params.pop("query")
    
    path2 = f"/movie/{movie_id}/credits"
    res2 = requests.get(BASE_URL+path2, params=params).json()
    cast_list = []
    crew_list = []
    for cast in res2.get("cast"):
        if cast.get("cast_id") < 10:
            cast_list.append(cast.get("name"))
    for crew in res2.get("crew"):
        if crew.get("department") == "Directing":
            crew_list.append(crew.get("name"))
            
    return {
        "cast": cast_list,
        "crew": crew_list,
    }
    

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화 id를 통해 영화 상세정보를 검색하여 주연배우 목록(cast)과 스태프(crew) 중 연출진 목록 반환
    영화 검색에 실패할 경우 None을 반환
    """
    pprint(credits('기생충'))
    # {'cast': ['Song Kang-ho', 'Lee Sun-kyun', ..., 'Jang Hye-jin'], 'crew': ['Bong Joon-ho', 'Park Hyun-cheol', ..., 'Yoon Young-woo']}
    pprint(credits('검색할 수 없는 영화'))
    # None
