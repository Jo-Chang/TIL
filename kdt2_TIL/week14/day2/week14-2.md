# Week14-2

-   Django - ORM, ORM with views


<link rel="stylesheet" href="../../assets/stylesheets/my_style.css">

<br>[Parent Contents...](../../README.md/#til-today-i-learned)


## Contents
- [sample](#sample)

<br>


-----


## ORM Edit

### ORM UPDATE

```py shell
# 수정할 인스턴스 조회
>>> article = Article.objects.get(pk=1)

# 인스턴스 변수를 변경
>>> article.title = 'byebye'

# 저장
>>> article.save()

# 정상적으로 변경
>>> article.title
'byebye'
```

### ORM DELETE

```py shell
# 수정할 인스턴스 조회
>>> article = Article.objects.get(pk=1)

# delete 메서드 호출 (삭제 된 객체 반환)
>>> article.delete()
(1, {'articles.Article': 1})

# 삭제한 데이터는 더이상 조회할 수 없음
>>> Article.objects.get(pk=1)
DoesNotExist: Article matching query does not exist
```


-----


## ORM with view

- 사전 준비
  + app URLs 분할 및 연결
  + index 페이지 작성

### READ

- [전체 게시글 조회](lecture/articles/views.py)
  ```py
  # articles/views.py
  from django.shortcuts import render
  from .models import Article

  # Create your views here.
  def index(request):
      articles = Article.objects.all()
      context = {
          'articles': articles,
      }
      return render(request, 'articles/index.html', context)
  ```
  ```html
  <!-- articles/index.html -->

  <h1>Articles</h1>
  <hr>
  {% for article in articles %}
    <p>글 번호: {{ article.pk }}</p>
    <p>글 번호: {{ article.pk }}</p>
    <p>글 번호: {{ article.pk }}</p>
  {% endfor %}
  ```

- [단일 게시글 조회](lecture/articles/views.py)


-----


## CREATE

- Create 로직을 구현하기 위해 필요한 view 함수
  + new - 사용자의 입력을 받는 페이지를 렌더링
  + create - 사용자가 입력한 데이터를 받아 DB에 저장

- 주의 사항 (유효성 검사)
  ```py
  # 받은 데이터를 DB에 저장
  # sol1
  """
  article = Article()
  article.title = title
  article.content = content
  article.save()
  """
  
  # sol2
  # 저장 전 유효성 검사와 같은 추가 작업을 위해 2번 선택
  article = Article(title=title, content=content)
  article.save()
  
  # sol3
  """
  article = Article.objects.create(title=title, content=content)
  """
  ```


-----


## Tips

- Django `en-us` to `ko-kr` & `UTC` to `한국표준시각`
  ```py
  # Internationalization
  # https://docs.djangoproject.com/en/3.2/topics/i18n/

  # LANGUAGE_CODE = 'en-us'
  LANGUAGE_CODE = 'ko-kr'

  # TIME_ZONE = 'UTC'
  TIME_ZONE = 'Asia/Seoul'

  ...
  ```