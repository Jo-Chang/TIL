# Week16-2

-   Djgno - Many to one relationships 1


<link rel="stylesheet" href="../../assets/stylesheets/my_style.css">

<br>[Parent Contents...](../../README.md/#til-today-i-learned)


## Contents
- [sample](#sample)

<br>


-----


## Introduction

- Relational DB의 N:1
![Relational DB N-1](assets/01.JPG)

- Foreign Key - 테이블의 필드 중 다른 테이블의 레코드를 식별할 수 있는 키
  + 각 레코드에서 서로 다른 테이블 간의 '관계'를 만드는 데 사용


-----


## Comment & Article

- Many to one relationships : 한 테이블의 0개 이상의 레코드가 다른 테이블의 레코드 한 개와 관련된 관계
  + N:1 or 1:N
  > Comment(댓글)[N] - Article(게시글)[1]

- Comment 모델 정의
  + ForeignKey 클래스를 작성하는 위치와 관계없이 필드 마지막에 생성됨
```py
# articles/models.py

class Comment(models.Model):
  article = models.ForeignKey(Article, on_delete=models.CASCADE)
  content = models.CahrField(max_length=200)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
```

- `on_delete` - 외래 키가 참조하는 객체가 사라졌을 때, 외래 키를 가진 객체 처리 설정(데이터 무결성 조건에 의거)
  + `CASCADE` - 부모 객체(참조 된 객체)가 삭제 됐을 때 이를 참조하는 객체도 삭제
  + `PROTECT` - ...
  + `RESTRICT` - ...
  + `SET_NULL`, `SET_DEFAULT`, `SET()`, `DO_NOTHING`
  > https://docs.djangoproject.com/en/4.2/ref/models/fields/#django.db.models.ForeignKey.on_delete

- 역참조 - 자신을 참조하는 테이블(자신을 외래키로 지정한)을 참조하는 것
  + N:1에서 1이 N을 참조하는 상황

- `article.comment_set.all()`
  + article - 모델 인스턴스
  + comment_set - related manager
  + all() - QuertSet API
  + 의미론적으로 `Comment.objects.filter()`보다 완벽함 / SQL 쿼리문 자체는 동일

- Comment CREATE
  + `save(commit=False)` - DB에 저장하지 않고 인스턴스만 반환
```py
# articles/views.py

def comments_create(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    comment_form = CommentForm(data=request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.article = article
        # comment.save()    # 가능
        comment_form.save()
        return redirect('articles:detail', article_pk)
    
    context = {
        'article': article,
        'comment_form': comment_form,
    }
    return render(request, 'articles/detail.html', context)
```

- Comment DELETE


-----


## Tips

- Django Cleanup
  + 유저가 삭제한 미디어 파일 같이 삭제하는 라이브러리

- 댓글 개수 출력하기
  + DTL filter - length 사용
```py
{{ comments|length }}

{{ article.comment_set.all|length }}
```
  + QuerySetAPI - count() 사용
```py
{{ article.comment_set.count }}
```

- 댓글이 없는 경우 대체 컨텐츠
```html
<!-- articles/detail.html -->


```

- 댓글 수정의 미구현 이유
  + 현재 페이지를 유지한 상태로 Form부분만 변경되어 수정해야 하므로 JavaScript의 영역

- html <nobr> 태그