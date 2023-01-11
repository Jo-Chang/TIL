import json
# from pprint import pprint

with open("data/movie.json", "r", encoding = "UTF8") as f:
    movie = json.load(f)
    list = [
        "id",
        "title",
        "vote_average",
        "overview",
        "genre_ids",
    ]
    dict_var = {}
    for str in list:
        dict_var[str] = movie[str]
        
    print(dict_var)


"""_answer_
import json

# 아래 코드 수정 금지
movie_json = open('data/movie.json', encoding='UTF8')
movie = json.load(movie_json)

# 이하 문제 해결을 위한 코드 작성
new_movie = {
    'id': movie['id'],
    'title': movie['title'],
    'vote_average': movie['vote_average'],
    'overview': movie['overview'],
    'genre_ids': movie['genre_ids'],
}
print(new_movie)
"""
