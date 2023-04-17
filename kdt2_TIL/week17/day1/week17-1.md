# Week17-1

-   Django - Many to many relationships 1


<link rel="stylesheet" href="../../assets/stylesheets/my_style.css">

<br>[Parent Contents...](../../README.md/#til-today-i-learned)


## Contents
- [sample](#sample)

<br>


-----


## Outline

- M:N 관계
  + 환자 - 의사 병원진료 시스템 모델


-----


## Django ManyToManyField

- Django ManyToManyField
```py
# hospitals/models.py

class Patient(models.Model):
  doctors = models.ManyToManyField(to=Doctor)
  name = models.TextField()
```

- `through` argument
  + 중개 모델을 지정하여 추가 정보를 더하기 위함
  + ex) 환자 진단 증상 정보
```py
class Patient(models.Model):
    doctors = models.ManyToManyField(to=Doctor, through='Reservation')
    name = models.TextField()


class Reservation(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    symptom = models.TextField()
    reserved_at = models.DateTimeField(auto_now_add=True)
```

- summary
  + M:N 관계로 맺어진 두 테이블에는 변화 없음
  + ManyToManyField는 중개 테이블을 자동으로 생성함
  + 두 모델 중 어느쪽에 위치해도 무관하나, 참조와 역참조 방향 주의

- `related_name` - 역참조시 사용하는 manager name을 변경
```py
class Patient(models.Model):
  doctors = models.ManyToManyField(Doctor, related_name='patients')
  name = models.TextField()

# 변경 전
doctor.patient_set.all()

# 변경 후
doctor.patients.all()
```

- `symmetrical` : 자기 자신과의 M:N 관계
  + 기본 값 : True
  + True일 경우
    * _set 매니저를 추가 하지 않음
    * source 모델의 인스턴스가 target 모델의 인스턴스를 참조하면 자동으로 target 모델 인스턴스도 source 모델 인스턴스를 자동으로 참조하도록 함(대칭)
  + 대칭을 원하지 않는 경우 False로 설정
    * Follow 기능 구현에서 다시 확인할 예정
```py
class Person(models.Model):
  friends = models.ManyToManyField('self')
  # friends = models.ManyToManyField('self', symmetrical=False)
```

- `add()` : 지정된 객체를 관련 객체 집합에 추가
 + 이미 존재하는 관계에 사용하면 관계가 복제되지 않음

- `remove()` : 관련 객체 집합에서 지정된 모델 개체를 제거


-----


## Articles & Users

- Article(M) - User(N) : 0개 이상의 게시글은 0명 이상의 회원과 관련된다.

```py
# articles/models.py

class Article(models.Model):
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(to=settings.AUTH_USER_MODEL, related_name='like_articles')
    # related_name이 없을 경우 위 user와 manager name이 동일하여 migration 오류가 발생함.
    
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```

```py
# articles/urls.py

urlpatterns = [
  ...
  path('<int:article_pk>/likes/', views.likes, name='likes'),
]
```
```py
# articles/views.py

@login_required
def likes(request, article_pk):
  article = Article.objects.get(pk=article_pk)
  if request.user in article.like_users.all():
    article.like_users.remove(request.user)
  else:
    article.like_users.add(request.user)
  return redirect('articles:index')
```
```html
<!-- articles/index.html -->

{% for article in articles %}
  ...
  <form action="{% url 'articles:likes' article.pk %}" method="post" class="">
    {% csrf_token %}
    {% if request.user in article.like_users.all %}
    <input type="submit" value="좋아요 취소" class="">
    {% else %}
    <input type="submit" value="좋아요" class="">
    {% endif %}
  </form>
{% endfor %}
```

- `.exists()` - QuerySet에 결과가 포함되어 있으면 True 아니면 False
  + 큰 QuerySet에 있는 특정 개체 존재 검색 시 효율적
```py
# articles/views.py

@login_required
def likes(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    if article.like_users.filter(pk=request.user.pk).exists():
        article.like_users.remove(request.user)
    else:
        article.like_users.add(request.user)
    return redirect('articles:index')
```