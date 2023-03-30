# Week14-3

-   Django - ORM with view


<link rel="stylesheet" href="../../assets/stylesheets/my_style.css">

<br>[Parent Contents...](../../README.md/#til-today-i-learned)


## Contents
- [sample](#sample)

<br>


-----


## HTTP request methods

- redirect() : 인자에 작성된 주소로 다시 요청을 보냄
  ```py
  from django.shortcuts import render, redirect


  def create(request):
    title = request.GET.get('title')
    title = request.GET.get('title')
    article = Article(title=title, content=content)
    article.save()

    return redirect('articleS:detail', article.pk)
  ```

- HTTP : 네트워크 상에서 데이터를 주고 받기위한 약속

- GET & POST - 데이터(리소스)에 어떤 요청(행동)을 원하는지를 나타내는 것

- `GET` Method : 특정 리소스를 조회하는 요청
  + GET으로 데이터를 전달하면 <span>Query String</span> 형식으로 보내짐
  + 데이터를 가져올때만 사용

- `POST` Method : 특정 리소스에 변경사항을 만드는 요청
  + POST로 데이터를 전달하면 <span>HTTP Body</span>에 담겨 보내짐
  + POST Method는 DB에 대한 변경사항을 만드는 요청이기 때문에 토근을 사용해 최소한의 신원 확인 필요

- HTTP response statue code : 특정 HTTP 요청이 성공적으로 완료되었는지 알려줌
  + 5개의 그룹으로 나뉘어짐 (1xx, 2xx, 3xx, 4xx, 5xx)
  >https://developer.mozilla.org/en-US/docs/Web/HTTP/Status
  + 403 Forbidden - 서버에 요청이 전달되었지만, 권한 때문에 거절되었다는 것을 의미

- CSRF ( Cross-Site-Request-Forgery ) : 사이트 간 요청 위조
  + 사용자가 자신의 의지와 무관하게 공격자가 의도한 행동을 하여 특정 웹 페이지를 보안에 취약하게 하거나 수정, 삭제 등의 작업을 하게 만드는 공격 방법

- Security Token (CSRF Token) : 대표적인 CSRF 방어 방법
  + 서버는 사용자 입력 데이터에 임의의 난수 값(token)을 부여
  + 매 요청마다 해당 token을 포함시켜 전송 시키도록 함
  + 이후 서버에서 요청을 받을 때마다 전달된 token이 유효한지 검증


-----


## DELETE

```py
# articles/urls.py

urlpatterns = [
  ...,
  path('<int:pk>/delete/', views.delete, name='delete'),
]
```
```py
# articles/views.py

def delete(request, pk):
  article = Article.objects.get(pk=pk)
  article.delete()
  return redirect('articles:index')
```
```html
<!-- articles/detail.html -->

<body>
  <h2>DETAIL</h2>
  ...
  <hr>
  <form action="{% url 'artidles:delete' article.pk %}" method="POST">
    {% csrf_token %}
    <input type="submit" value="DELETE">
  </form>
  <a href="{% url 'articles:index' %}">[back]</a>
</body>
```


-----


## Update

- `edit` - 사용자의 입력을 받는 페이지를 렌더링

- `update` - 사용자가 입력한 데이터를 받아 DB에 저장


-----


## Tips

- [Premonition] REST API
  + (POST) articles/1/  ->  1번 게시글 생성
  + (PATCH) articles/1/  ->  1번 게시글 수정
  + (DELETE) articles/1/  ->  1번 게시글 삭제
  + HTTP request methods를 활용한 효율적인 URL 구조