# Week16-1

-   Django - Static files


<link rel="stylesheet" href="../../assets/stylesheets/my_style.css">

<br>[Parent Contents...](../../README.md/#til-today-i-learned)


## Contents
- [sample](#sample)

<br>


-----


## Introduction

- Static Files - 서버 측에서 변경되지 않고 고정적으로 제공되는 파일
  + 이미지, JS, CSS 파일 등

- 웹 서버의 기본 동작
  + 특정 위치(URL)에 자원을 요청(HTTP request) 받아서
  + 응답(HTTP response)을 처리하고 제공(serving)하는 것
  + 웹 서버는 요청 받은 URL로 서버에 존재하는 정적 자원(static resource)을 제공함
  + 정적 파일을 제공하기 위한 경로(URL)가 있어야 함


-----


## Static files 제공하기

- 경로에 따른 Static file
  + 기본 경로 - `app/static`
  + 추가 경로 - `STATICFILES_DIRS`

- URL + STATIC_URL + 정적파일 경로
  > http://127.0.0.1:8000 + /static/ + articles/sample-1.png

- 추가 경로
```py
# settings.py

STATICFILES_DIRS = [
  BASE_DIR / 'static',
]
```


-----


## Media Files

- Media Files : 사용자가 웹에서 업로드하는 정적 파일 (user-uploaded)

- `ImageField()` - 이미지 업로드에 사용하는 모델 필드

- Prepare
  + settings.py에 MEDIA_ROOT, MEDIA_URL 설정
  + 작성한 MEDIA_ROOT와 MEDIA_URL에 대한 url 지정

- MEDIA_ROOT - 미디어 파일들이 위치하는 디렉토리의 절대 경로
```py
# settings.py

MEDIA_ROOT = BASE_DIR / 'media'
```

- MEDIA_URL - MEDIA_ROOT에서 제공되는 미디어 파일에 대한 주소를 생성(STATIC_URL과 동일한 역할)
```py
# settings.py

MEDIA_URL = '/media/'
```

- url 지정
```py
# crud/urls.py

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
  path(...),
  ...
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
```

-----


## 이미지 업로드 및 제공하기

- 이미지 업로드
```py
# articles/models.py

class Article(models.Model):
  title = ...
  ...
  image = models.ImageField(blank=True)
  ...
```

- migration 진행
```sh
$ pip install pillow
$ python manage.py makemigrations
$ python manage.py migrate
```

- form 요소의 enctype 속성 추가
```html
<!-- articles/create.html -->

<h1>CREATE</h1>
<form action="..." ... enctype="multipart/form-data">
  ...
</form>
```

- view 함수에 추가 코드 작성
```py
# articles/views.py

def create(request):
  if request.method == 'POST':
    form = ArticleForm(request.POST, request.FILES)
    ...
```

- 업로드 된 이미지 제공하기
```html
<!-- articles/detail.html -->

{% if article.image %}
    <img src="{{ article.image.url }}" alt="">
{% endif %}
```

- Django에서 파일의 겹쳐진 이름은 랜덤 해쉬값을 추가해서 이름 중복을 피한다


-----


## Tips

- `upload_to argument` - ImageField()의 upload_to 인자를 사용해 미디어 파일 추가 경로 설정
```py
# 1
image = models.ImageField(blank=True, upload_to='images/')

# 2
image = models.ImageField(blank=True, upload_to='images/')

# 3
def articles_image_path(instance, filename):
  return f'images/{instance.user.username}/{filename}'
image = models.ImageField(blank=True, upload_to='images/')
```

- Django Image Resizing
> https://django-imagekit.readthedocs.io/en/latest/