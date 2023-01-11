# JSON
-   자바스크립트 객체 표기법
-   개발 환경에서 많이 활용되는 데이터 양식
-   웹 어플리케이션에서 데이터를 전송할 때 일반적으로 사용
-   문자 기반(텍스트) 데이터 포멧으로 다수의 프로그래밍 환경에서 쉽게 활용 가능

> ***`movie.json`***
```json
{
    "adult": false,
    "backdrop_path": "/tXHpvlr....jpg",
    "genre_ids": [
        18,
        80
    ],
    "id": 278,
    "original_language": "en",
    "original_title": "The Shawshank Redemption",
    // ...
    "vote_count": 18040
}
```

> ***In python...***
```python
import json
x = [1, 'simple', 'list']
json.dumps(x)
```
```python
x = json.load(f)
```

``````python
import json
with open("data/movie.json", "r", encoding = "UTF8") as f:
    movie = json.load(f)
    print(movie)
    print(type(movie))
    print(movie['original_title'])
```

