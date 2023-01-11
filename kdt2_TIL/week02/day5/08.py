import json

# 아래 코드 수정 금지
movie_json = open('data/movie.json', encoding='UTF8')
movie = json.load(movie_json)

genres_json = open('data/genres.json', encoding='UTF8')
genres_list = json.load(genres_json)

genre_list2 = []
for genre_id in movie["genre_ids"]:
    for genre_id2 in genres_list:
        if genre_id2["id"] == genre_id:
            genre_list2.append(genre_id2["name"])
            
movie.pop("genre_ids")
movie.update({"genre_name": genre_list2})
print(movie)

'''
new = {
    "id": movie["id"],
    "title": movie["title"],
    "vote_average": movie["vote_average"],
    "overview": movie["overview"],
    "genre_names": genre_names,
}

print(new)
'''