from dotenv import load_dotenv, dotenv_values

# ref) https://github.com/theskumar/python-dotenv

print(load_dotenv("movie.env"))
print(load_dotenv("movie2.env"))
config = dotenv_values("movie.env")
print(config)
print(config.get("API_KEY"))