# Week14-4

-   Project - django-accountbooks


<link rel="stylesheet" href="../../assets/stylesheets/my_style.css">

<br>[Parent Contents...](../../README.md/#til-today-i-learned)


## Contents
- [sample](#sample)

<br>


-----


## 개선할 점

- 가계부 분류(category) select 태그 활용하여 입력 받기
- 가계부 분류에 따라 다른 디자인
- 가계부 분류별 조회
- 특정 기준으로 정렬해서 조회
```py
# settings.py
INSTALLED_APPS = [
  ...,
  'django.contrib.humanize',
  ...
]
```
```py
# index.html
{% extends ... %}
{% load humanize %}

...
{{ intVar|incomma }}
```
```html
<!-- detail.html -->
<input type="number" ... step="1000">
```