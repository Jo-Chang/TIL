# Week12-4

-   JavaScript - Controlling event


<link rel="stylesheet" href="../../assets/stylesheets/my_style.css">

<br>[Parent Contents...](../../README.md/#til-today-i-learned)


## Contents
- [sample](#sample)

<br>


-----


## Event

- Event : 무언가 일어났다는 신호, 사건
  + 모든 DOM 요소는 이러한 신호를 만들어 냄
  + 마우스, 인풋, 키보드, 터치 등

- Event Handler : Event 발생 시 실행되는 함수

- `.addEventListener()` : 대표적인 event handler
  + 특정 event를 DOM 요소가 수신할 떄마다 콜백 함수를 호출
  ```js
  EventTarget.addEventListerner(type, handler)
  /*
  EventTarget - DOM 요소
  type - 특정 이벤트
  handler - 콜백 함수
  */
  ```

- **click** event : 클릭 시 발생하는 이벤트

- **input** event : 텍스트 입력 시 발생하는 이벤트

- event cancel
  + `.preventDefault()` : 현재 Event의 기본 동작을 중단

- Lodash : JS의 라이브러리 중 하나, array, object등 자료구조 다루는 함수 제공