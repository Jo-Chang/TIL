# Week13-3

-   Django - Django Template


<link rel="stylesheet" href="../../assets/stylesheets/my_style.css">

<br>[Parent Contents...](../../README.md/#til-today-i-learned)


## Contents
- [Template](#template-system)
- [Inheritance](#template-inheritance)
- [Request & Response](#request--response-with-html-form)

<br>


-----


## Template System

- django template system : 데이터 <span>표현</span>을 제어하면서, 표현과 관련된 로직을 담당

- HTML의 특정 부분을 변수 값에 따라 바꾸고 싶을 떄
  ```html
  <body>
    <h1>Hello, django</h1>
  </body>
  ```
  ```python
  
  def index(request):
    context = {
      'name': 'Sophia',
    }
    return render(request, 'articles/index.html', context)
  ```
  ```html
  <body>
    <h1>Hello, {{ name }}</h1>
  </body>
  ```

- Django Template Language (DTL) : Template에서 조건, 반복, 변수, 필터 등의 프로그래밍적 기능을 제공하는 시스템

### DTL Syntax

- DTL Syntax
  + Variable
  + Filters
  + Tags
  + Comments

- Variable
  + view 함수에서 render 함수의 세번째 인자로 <span>딕셔너리 타입</span>으로 넘겨 받을 수 있음
  + 딕셔너리 key에 해당하는 문자열이 template에서 사용 가능한 변수명이 됨
  + dot(.)를 사용하여 변수 속성에 접근 가능
  ```python
  {{ vairable }}
  ```

- Filters
  + 표시할 변수 수정
  + chained가 가능하며 일부 필터는 인자를 받기도 함 `{{ name|truncatewords:30 }}`
  + 약 60개의 build-in template filters를 제공
  ```python
  {{ variable|filter }}
  ```

- Tags
  + 반복 또는 논리를 수행하여 제어 흐름을 만드는 등 변수보다 복잡한 일들을 수행
  + 일부 태그는 시작과 종료 태그 필요 `{% if %} {% endif %}`
  + 약 24개의 build-in template tags

- Comments
  + DTL에서의 주석 표현
  ```html
  <h1>Hello, {# name #}</h1>
  ```
  ```python
  {% comment %}
    {% if name == 'Sophia' %}
    {% endif %}
  {% endcomment %}
  ```


-----


## Template Inheritance

- 템플릿 상속 ( Template Inheritance ) : 페이지의 공통요소를 포함하고 하위 템플릿이 재정의 할 수 있는 공간을 정의하는 기본 <span>'skeleton' 템플릿</span>을 작성하여 상속 구조를 추구
  ```html
  <!-- articles/base.html -->
  <!doctype html>
  <html lang="en">
    <head>
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width, initial-scale=1">
      <title>Bootstrap demo</title>
      <!-- bootstrap CDN -->
    </head>
    <body>
      <h1>Hello, world!</h1>
      {% block content %}
      {% endblock content %}
      <!-- bootstrap CDN -->
    </body>
  </html>
  ```

- `extends` tag
  + 자식(하위) 템플릿이 부모 템플릿을 확장한다는 것을 알림
  + 반드시 <span>템플릿 최상단</span>에 작성되어야 함 (<span>2개 이상 사용 불가</span>)
  ```python
  {% extends 'path' %}
  ```

- `block` tag
  + 하위 템플릿에서 재정의(overridden)할 수 있는 블록을 정의
  + 하위 템플릿이 작성할 수 있는 공간을 지정
  ```python
  {% block name %}{% endblock name %}
  ```


-----


## request & response with HTML form

- 데이터를 보내고 가져오기 ( Sending and Retrieving form data )
  + HTML form element를 통해 <span>사용자와 애플리케이션 간의 상호작용</span> 이해

- `form` element
  + 사용자로부터 할당된 데이터를 서버로 전송
  + 웹에서 사용자 정보를 입력하는 여러 방식(text, password 등)을 제공
  + method 속성 기본 값 `GET`
  + <span>로그인 때 GET 방식 쓰면 url에 id, pwd 노출</span>

- `action` & `method`
  + form의 핵심 속성 2가지
  + 데이터를 어디(<span>action</span>)로 어떤 방식(<span>method</span>)으로 보낼지
  + 사용자 입력 데이터 key-value를 url에 추가한 형식으로 인식
  + action : 입력 데이터가 전송될 url을 지정 (목적지)
  + method : 데이터를 어떤 방식으로 보낼 것인지 정의, 데이터의 HTTP request methods (GET, POST)를 지정

- `input` element
  + 사용자의 데이터를 입력 받을 수 있는 요소
  + type 속성 값에 따라 다양한 유형의 입력 데이터를 받음

- `name`
  + input의 핵심 속성
  + 데이터를 제출했을 때 서버는 name 속성에 설정된 값을 통해 사용자가 입력한 데이터에 접근할 수 있음

- Query String Parameters
  + 사용자의 입력 데이터를 URL 주소에 파라미터를 통해 넘기는 방법
  + 문자열은 앰퍼샌드(&)로 연결된 key=value 쌍으로 구성, 기본 URL과 물음표(?)로 구분
  > ex) http://host:port/path?<span>key=value&key=value</span>


-----


## Tips

- 추가 템플릿 경로 지정

  ```python
  # settings.py

  TEMPLATES = [
    {
      'BACKEND': 'django.template...',
      'DIRTS': [BASE_DIR / 'templates',], # 사용자 지정 템플릿
      'APP_DIRS': True,
      'OPTIONS': {
        ...
      },
    }
  ]
  ```
