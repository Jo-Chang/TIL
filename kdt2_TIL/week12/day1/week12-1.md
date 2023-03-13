# Week12-1

-   History of Javascript


<link rel="stylesheet" href="../../assets/stylesheets/my_style.css">

<br>[Parent Contents...](../../README.md/#til-today-i-learned)


-----


## JavaScript의 탄생

- 기존 Netscape 소속 개발자 Brandon Eich가 화사의 요구사항을 넘어 Mocha라는 언어를 개발

- 이후 LiveScript로 이름 변경했으나 당시에 인기있던 Java의 명성에 기대고자 JavaScript로 변경

- JavaScript 파편화
  + 당시 가장 강력하던 Microsoft의 Internet Explorer는 회사들이 자체적으로 JavaScript를 탑재해 독자적으로 업데이트함
  + 이로 인해 같은 코드가 브라우저 마다 다르게 동작하는 문제 발생 -> 크로스 브라우징 이슈
    * JavaScript의 표준화가 요구됨

- JavaScript 현황
  + Chrome, Firefox, Safari, Microsoft Edge 등 다양한 웹 브라우저 출시되었으며 다양화 됨
  + JavaSCript는 웹 페이지의 동적인 기능을 구현하는데 사용
  + Node.js와 같은 서버 사이드, 다양한 프레임워크와 라이브러리 제공으로 웹 개발 분야에서 필수적인 언어가 됨

- JavaScript의 표준화
  + ECMAScript : Ecma International<sup><span>(정보와 통신 시스템을 위한 국제적 표준화 기구)</span></sup>이 정의하고 있는 표준화된 스크립트 프로그래밍 언어
  
- JavaScript 표준화 역사
  + JavaScript의 파편화를 막기 위해 1997년 ECMA에서 ECMAScript라는 표준 언어를 정의
  + 이후 ECMAScript는 독자적으로 발전하며 JavaScript보다 더 많은 기능을 제공하게 됨
  + 2009년, ECMAScript 5 (ES5)에서 안정성과 생산성을 크게 높임
  + 2015년, ECMAScript 2015 (ES6)에서 객체지향 프로그래밍 언어로써 많은 발전을 이루어, <span>역사상 가장 중요한 버전</span>으로 평가됨
  + JavaScript는 ECMAScript의 구현 언어 중 하나


-----


## JavaScript 실행

- JavaScript 실행 환경
  + HTML script 태그
  ```html
  <body>
    <script>
      console.log('hello')
    </script>
  </body>
  ```
  + js 확장자 파일
  ```javascript
  console.log('hello')
  ```
  ```html
  <body>
    <script src="hello.js"></script>
  </body>
  ```
  + 브라우저 Console


-----


## DOM

- DOM ( Document Objective Model ) : 웹 페이지(Document)를 구조화된 객체로 제공하며 <span>프로그래밍 언어가 웹 페이지를 사용할 수 있게</span> 연결시킴

- **브라우저의 웹 페이지 로딩 과정** : 
문서(Document)는 웹 브라우저를 통해 해석되어 화면에 나타남, DOM은 이러한 문서를 조작하는 방법을 제공하는 <span>API</span>
  + 브라우저는 HTML 문서를 해석하여 <span>DOM tree</span>라는 객체의 트리로 구조화 함
  + DOM에서 모든 요소, 속성, 텍스트는 하나의 객체이며 모두 document 객체의 자식

```html
<!DOCTYPE html>
<html lang="en">

  <head>
    <title>Document</title>
  </head>

  <body>
    <h1>Heading</h1>
    <a href="https://www.google.com/">google</a>
  </body>

</html>
```
```dom
DOCTYPE: html
HTML lang="en"
  HEAD
    TITLE
      #text: Document
    #text:
  BODY
    #text:
    H1
      #text: Heading
    #text:
    A href="https://www.google.com/"
      #text: google
    #text:
```

- 웹 페이지를 동적으로 만드는 것 == 웹 페이지를 조작<sup><span>생성, 추가, 삭제</span></sup>하는 것
  + 조작하기 위한 순서
    1. 조작하고자 하는 요소를 <span>선택</span> 또는 <span>탐색</span>
    2. 선택된 요소의 콘텐츠 또는 속성을 <span>조작</span>

- 'document' object
  + 웹 페이지 객체
  + <span>DOM Tree의 진입점</span>
  + 페이지를 구성하는 모든 객체 요소 포함


### DOM Query

- DOM Query(선택문)
  + `document.querySelector()` : 요소 하나 선택
  + `document.querySelectorAll()` : 요소 여러 개 선택


### DOM Manipulation

- DOM Manipulation (조작)

- 'classList' property : 클래스 속성 조작, 요소의 클래스 목록을 DOMTkenList(유사 배열) 형태로 반환, add()와 remove() 메서드를 사용해 지정한 클래스 값을 추가 혹은 제거
  + element.classList.add() : 지정한 클래스 값 추가
  + element.classList.remove() : 지정한 클래스 값 삭제
  + 조회 `.getAttribute()` / 설정(수정) `.setAttribute()` / 삭제 `.removeAttribute()`

- 'textContent' property : HTML 콘텐츠 조작, 요소의 텍스트 콘텐츠를 표현

- DOM 요소 조작
  + 생성 `.createElement()` / 추가 `.appendChild()` / 삭제 `.removeChild()`

- 'style' property : 스타일 조작, 해당 요소의 모든 스타일 속성 목록을 포함하는 속성