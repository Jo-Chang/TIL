import json

# 아래 코드 수정 금지
movie_json = open('data/movie.json', encoding='UTF8')
movie = json.load(movie_json)

genres_json = open('data/genres.json', encoding='UTF8')
genres_list = json.load(genres_json)


### code
genre_name = []
for id in movie["genre_ids"]:
    for genre in genres_list:
        if genre["id"] == id:
            genre_name.append(genre["name"])

print(genre_name)