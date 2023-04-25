# Week18-2

-   Django - Rest Framework 2


<link rel="stylesheet" href="../../assets/stylesheets/my_style.css">

<br>[Parent Contents...](../../README.md/#til-today-i-learned)


## Contents
- [sample](#sample)

<br>


-----


## N:1 Relation

- Article(1) - Comments(N) 관계에 대한 Serializer 작성

- 역참조 데이터 조회
  + 정참조 조회 시에는 article과 같은 형태로 작성 가능
  + 기존 필드 override

- `PrimaryKeyRelatedField()`
  + 필드 이름 변경은 models.py 에서만 가능

- Nested relationships - 기존 필드에 다른 클래스 직접 추가

- 특정 필드 override 혹은 추가시 read_only_fields가 동작하지 않음


-----


## API 문서화

- Swagger - REST 웹 서비스를 설계, 빌드, 문서화 등을 도와주는 오픈소스 소프트웨어 프레임워크
> https://drf-yasg.readthedocs.io/en/stable/


-----


## Tips

- Django shortcuts functions
  + `render()`
  + `redirect()`
  + `get_object_or_404()`
  + `get_list_or_404()`
  + -> 클라이언트 입장에서 서버 오류(500)보다 예외 처리(404)가 적합함