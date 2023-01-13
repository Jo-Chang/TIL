import requests
from dotenv import dotenv_values

# TMDB token = {movie.env - API_KEY}
# https://api.themoviedb.org/3/movie/550?api_key=<<api_key>>

'''__movie.env__
# TMDB api_key
API_KEY=0000
'''

BASE_URL = "https://api.themoviedb.org/3"
path = "/movie/popular"
params = {
    "api_key": dotenv_values("movie.env").get("API_KEY"),
    "language": "ko-KR",
    "region": "KR",
}

response = requests.get(BASE_URL + path, params = params).json()
print(response)
print(response.get("results")[0])