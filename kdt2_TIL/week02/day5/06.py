import json
from pprint import pprint

with open("data/movies.json", "r", encoding = "UTF8") as f:
    movies_list = json.load(f)
    
data_list = [
    "id",
    "title",
    "poster_path",
    "vote_average",
    "overview",
    "genre_ids",
]

movies = []
for dict_var in movies_list:
    dict_var2 = {}
    for str in data_list:
        dict_var2[str] = dict_var[str]
    movies.append(dict_var2)

print("[")
for movie in movies:
    print("     {")
    for k, v in movie.items():
        print(f"        \"{k}\":{v}")
    print("     },")
print("]")