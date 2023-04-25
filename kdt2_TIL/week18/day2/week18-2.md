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

- Request Method 별 데코레이터 달리하는 법
> https://jinpyo-hong.tistory.com/5

### PUT vs PATCH (RFC 문서 기준)
- PUT : 요청한 URI에 payload에 있는 자원으로 <span>대체</span>
  + 요청한 URI 아래 자원이 존재하지 않는 경우 -> 새로운 자원으로 저장하고 201(Created) status response
  + 존재하는 경우 -> 대체 요청 적용 시 200(ok) status, 실패 시 204(no content) status
  + 예시) 좋아요/싫어요, 추천/비추천
  + PUT 메서드는 클라이언트가 해당 자원의 상태를 모두 알고 있다고 가정되어야 함 -> payload만으로 자원의 전체 상태를 알 수 있어야 함

- PATCH : 요청한 자원에 대한 <span>부분적인 수정</span>을 적용하는 메서드
  + {{고찰}} *댓글 기능에서 댓글 내용만 바꾸는 경우는 PATCH가 더 적절할지도..?*

- Idempotence (멱등성) : f(f(x)) = f(x), 연산을 여러번 진행한 후에 다시 자기 자신이 되는 성질

- 참고 문서
  > https://tecoble.techcourse.co.kr/post/2020-08-17-put-vs-patch/
  > 