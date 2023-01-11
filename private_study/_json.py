import json
from pprint import pprint

with open("_json.json", "r", encoding = "UTF8") as f:
    movie = json.load(f)
    print(movie)
    print(type(movie))
    print(movie['original_title'])
    
    print("=============")
    
    pprint(movie)
    # print(movie[0])