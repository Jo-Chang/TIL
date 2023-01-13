import requests
from pprint import pprint
import os
from dotenv import load_dotenv

def recommendation(title):
    pass
    # 여기에 코드를 작성합니다.
    load_dotenv("../python/movie.env", verbose=True)
    BASE_URL = "https://api.themoviedb.org/3"
    path1 = "/search/movie"
    params = {
        "api_key": os.getenv("API_KEY"),
        "language": "ko-KR",
        "region": "KR",
        "query": title,
    }
    # print(params)   # debug
    
    res1 = requests.get(BASE_URL+path1, params=params).json()
    if len(res1.get("results")) == 0:
        return None
    movie_id = res1.get("results")[0].get("id")
    
    path2 = f"/movie/{movie_id}/recommendations"
    params.pop("query")
    # print(params)   # debug
    
    res2 = requests.get(BASE_URL+path2, params=params).json()
    recommendation_list = []
    for movie in res2.get("results"):
        recommendation_list.append(movie.get("title"))
    return recommendation_list


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화의 id를 기반으로 추천 영화 목록 구성
    추천 영화가 없을 경우 []를 반환
    영화 검색에 실패할 경우 None을 반환
    (주의) 추천 영화의 경우 아래 예시 출력과 차이가 있을 수 있음
    """
    pprint(recommendation('기생충'))
    # ['조커', '1917', '조조 래빗', ..생략.., '살인의 추억', '펄프 픽션']
    pprint(recommendation('그래비티'))
    # []
    pprint(recommendation('검색할 수 없는 영화'))
    # None
