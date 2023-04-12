# Week16-3  

-   Django - Many to one relationships 2


<link rel="stylesheet" href="../../assets/stylesheets/my_style.css">

<br>[Parent Contents...](../../README.md/#til-today-i-learned)


## Contents
- [sample](#sample)

<br>


-----


## Introduction

- Article(N) - User(1)
  + 0개 이상의 게시글은 1개의 회원에 의해 작성 될 수 있음

- Comment(N) - User(1)
  + 0개 이상의 댓글은 1개의 회원에 의해 작성 될 수 있음


-----


## Article & User

- Article 모델에 User 외래 키 정의
  + User 모델 참조 방법 - Django 에서 User 모델 직접 참조를 강하게 금지한다
  + `get_user_model()`  - User Object 객체
  + `settings.AUTH_USER_MODEL` - accounts.User 문자열, models.py에서만 사용
  + Django 코드 구동 상 객체 생성 이전에 model을 참조할 수 있는 models.py에만 문자열로 정보 건내줌

-  Create
```py
# articles/views.py

@login_required
def create(request):
  if request.method == 'POST':
    form = ArticleForm(request.POST)
    if form.is_valid():
      article = form.save(commit=False)
      aritlce.user = request.user
      article.save()
      return redirect('articles:detail', article.pk)
  ...
```

- Update
```py
# articles/views.py

@login_required
def update(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    if request.user == article.user:
        if request.method == 'POST':
            form = ArticleForm(request.POST, instance=article)
            if form.is_valid():
                form.save()
                return redirect('articles:detail', article.pk)
        else:
            form = ArticleForm(instance=article)
    else:
        return redirect('articles:index')

    ...
```
```html
{% if request.user == article.user %}
  <form action="{% url 'articles:delete' article.pk  %}" method="POST">
    {% csrf_token %}
    <input type="submit" value="삭제">
  </form>
  <a href="{% url 'articles:update' article.pk %}">[UPDATE]</a>
{% endif %}
```

- Delete
```py
# articles/views.py

@login_required
def delete(request, artilce_pk):
    if request.user == article.user:
        article = Article.objects.get(pk=artilce_pk)
        article.delete()

    return redirect('articles:index')
```


-----


## Comment & User

- User 외래 키 정의

- Create
```py
# articles/views.py

def comments_create(...):
  ...
  if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.article = article
        comment.user = request.user
        # comment.save()    # 가능
        comment_form.save()
        return redirect('articles:detail', article_pk)
  ...
```

- Delete
```py
# articles/views.py

def comments_delete(...):
    comment = Comment.objects.get(pk=comment_pk)
    if request.user == comment.user:
        comment.delete()
    return redirect('articles:detail', article_pk)
```