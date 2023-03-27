# Django Setting Guide


## Basic Setting
1.  `$ python -m venv venv`
  + 가상환경 세팅

2.  `$ source ~/venv/Scripts/activate`
  + 가상환경 활성화

3.  `$ pip install django==3.2.18`
  + KDT 실습용 3.2.18(2023 LTS) 버전 django pip install

4.  `$ pip freeze > requirements.txt`
  + 가상환경 의존파일 txt파일화
  + 약속에 의거 'requirements.txt'로 권장 (s 주의)
  + 이후 `$ pip install -r requirements.txt`로 패키지 목록 설치

5.  `$ django-admin startproject {project name} .`
  + 프로젝트 폴더와 manage.py 생성
  + 맨 끝 '.'으로 현재 디렉토리에 생성

- 5-1. `$ python manage.py runserver`
  + 서버 작동 확인
  + port 8000번으로 localhost 접속 시 로켓 화면 GET하는지 확인


## App Setting
6.  `$ python manage.py startapp {app name}`
  + App 생성
  + 최초 articles 권장

7.  `/{project name}/settings.py`에서 INSTALLED_APPS에 `{app name}` 추가
  + startapp으로 app 먼저 생성하고 추가 권장

- 7-1. `/{project name}/settings.py`에서 TEMPLATES > DIRS에 `[BASE_DIR / '{common templates}',],`로 템플릿 경로 추가 가능


## URL Setting
8.  `/{project name}/urls.py`에 `from {app name} import views`로 import하고 urlpatterns에 `path('{path name}/', views.{function name}),` 추가

- 8-1. `/{project name}/urls.py`에 app_name = '{app name}'으로 app_name 지정 가능

- 8-2. `/{project name}/urls.py`에 `from django.urls import path, include` 추가하고 `path('{app name}/', include('{app name}.views'),`로 App URL mapping 가능

- 8-3. `/{app name}/urls.py`에 `from . import views`로 import하고 
`path('{path name}/', views.{function name}, name='{call name}'),`으로 URL naming 가능

- 8-4. 모든 네이밍이 완료된후 템플릿에서 `{% url '{{app_name}:{call name}}' %}`으로 경로 무관하게 호출 가능
  + form의 action이나 a의 href 등에서 사용 가능


## Template Setting
9.  `/{app name}/templates/{app name}/` 경로에 파일 추가하고 views.py에서 return render(request, '{Template Path}', context)로 추가 가능
  + Context는 템플릿에 전달할 변수 Dictionary 형식으로 전달 가능

10. 공용 템플릿인 base.html 만들면 편리
  + `{% extends 'base.html' %}` 형식으로 공용 템플릿 호출
  + base.html에 `{% block {name} %}{% endblock {name} %}` 생성해두고 다른 템플릿 html에서 같은 형식으로 호출


## Model Setting
11. `{app name}/models.py`에 설계도 작성
  + class 이름이 테이블 이름
  + 변수 이름이 필드 이름
  + 변수 값은 `models.{type}Field(...)`으로 필드 속성 설정

12. `$ python manage.py makemigrations`로 `{app name}/migrations/`에 설계도 자동 생성

13. `$ python manage.py migrate`로 설계도 DB에 적용


## Admin Setting
14. `$ python manage.py createsuperuser`
  + 관리자

15. `{app name}/admin.py`에 `from .models import {class name}` / `admin.site.register({class name})` 추가