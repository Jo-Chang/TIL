# JavaScript
-   JavaScript : 웹페이지를 동적으로 프로그래밍적으로 제어하기 위한 언어
>   ref) [생활코딩 - JavaScript](https://opentutorials.org/course/743)

## Contents
- []()
    + []()
- [Javascript Tutorial](#javascript-can-do)
- [Datatype](#datatype)
    + [int](#정수형-실수형-숫자)
    + [string](#문자)

---

## JavaScript can do...
-   웹페이지 스크립팅 - DOM
-   서버 측 스크립팅 - node.js
-   브라우저 확장기능
-   Adobe PDF
-   Unity 게임 엔진
-   채팅 시스템

## Example code
```JavaScript
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8"/>
    </head>
    <body>
        <script>
            alert('Hello world');
        </script>
    </body>
</html>
```

---

## Datatype
### 정수형, 실수형 숫자
-   basic operations : +, -, *, /
-   지원 함수 : pow() / round() / ceil() / floor() / sqrt() / random()
    ```JavaScript
    Math.pow(3, 2);     // # 9  | 3의 2승
    Math.round(10.6);   // # 11 | 10.6 반올림
    Math.ceil(10.2);    // # 11 | 10.2 올림
    Math.floor(10.6);   // # 10 | 10.6 내림 
    Math.sqrt(9);       // # 3  | 9의 제곱근
    Math.random();      // # (0부터 1.0 사이의 랜덤한 숫자)
    ```
### 문자
-   **"** 혹은 **'** 중 하나로 시작해서 하나로 끝나야 함
    ```javascript
    alert("coding everybody");
    alert('coding everybody');
    ```
    ```javascript
    alert(typeof "1")
    // # string
    alert(typeof 1)
    // # number
    ```
-   따옴표 안에 따옴표를 포함시킬때 다음과 같이 포함 : `\'` 혹은 `\"`
-   줄바꿈 : `"\n"`
    ```javascript
    alert("안녕하세요. \n 생활코딩과 함께하는 JavaScript!");
    // # 안녕하세요.
    // #  생활코딩과 함께하는 JavaScript!
    ```
-   문자와 문자 더하기 지원
    ```javascript
    alert("coding" + " everybody");
    // # coding everybody
    ```
-   문자의 길이 : .length
    ```javascript
    alert("coding everybody".length)
    // # 16
    ```

---

## 