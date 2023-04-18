# Week17-2

-   Django - Many to many relationships, Fixtures


<link rel="stylesheet" href="../../assets/stylesheets/my_style.css">

<br>[Parent Contents...](../../README.md/#til-today-i-learned)


## Contents
- [sample](#sample)

<br>


-----


## Many To Many

- Profile 구현
```py
# accounts/views.py

from django.contrib.auth import get_user_model

def profile(request, username):
    User = get_user_model()
    person = User.objects.get(username=username)
    context = {
        'person': person,
    }
    return render(request, 'accounts/profile.html', context)
```

### User & User

- User(M) - User(N) -> 유저는 0명 이상의 다른 유저와 관련된다.
```py
# accounts/models.py

class User(AbstractUser):
  followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
```


-----


## Fixtures

- fixtures - Django가 DB로 가져오는 방법을 알고있는 데이터 모음
  + 모델에 초기 데이터 제공
  + Initial Data

- dumpdata : DB의 모든 데이터를 출력
  + 여러 모델을 하나의 json 파일로 만들 수 있음
```sh
$ python manage.py dumpdata [app_name[.ModelName] [app_name[.ModelName] ...]] > filename.json
```
```sh
$ python manage.py dumpdata --indent 4 articles.article > articles.json
```
```sh
$ python manage.py dumpdata --indent 4 articles.user > users.json
$ python manage.py dumpdata --indent 4 articles.comment > comments.json
```
```sh
# 3개의 모델 한번에 하나의 json 파일로
$ python manage.py dumpdata --indent 4 articles.article articles.comment accounts.user > data.json

# 모든 모델을 하나의 json 파일로
$ python manage.py dumpdata --indent 4 > data.json
```

- loaddata : fixtures 데이터를 DB로 불러오기
```sh
$ python manage.py loaddata articles.json users.json comments.json
```
  + utf-8 codec 오류 발생
  
  1. dumpdata 시 추가 옵션 작성
```sh
$ python -Xutf8 manage.py dumpdata [생략]
```
  2. 메모장 활용
    * 메모장으로 json 파일 열고 인코딩을 UTF8로 변경하며 저장