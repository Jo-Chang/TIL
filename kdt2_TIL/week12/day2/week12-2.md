# Week12-2

-   Basic syntax of JavaScript


<link rel="stylesheet" href="../../assets/stylesheets/my_style.css">

<br>[Parent Contents...](../../README.md/#til-today-i-learned)


-----


## Variable

- 식별자(변수명) 작성 규칙
  + 반드시 문자, 달러($) 또는 밑줄(_)로 시작
  + 대소문자 구분, 클래스명 외에는 모두 소문자로 시작
  + 예약어 사용 불가 `for, if, function, ...`

- 식별자(변수명) 작성 규칙
  + 카멜 케이스(camelCase) - 변수, 객체, 함수에 사용
  + 파스칼 케이스(PascalCase) - 클래스, 생성자에 사용
  + 대문자 스네이크 케이스(SNAKE_CASE) - 상수(constants)에 사용

- 변수 선언 키워드
  + let
  + const
  + var
  > <span><sup>let, const는 ES6(2015년, 주사용 버전)에서 추가됨</sup></span>

### let

- 블록 스코프를 갖는 <span>지역 변수</span> 선언
- 재할당 가능 & 재선언 불가능
```js
let number = 10 // 1. 선언 및 초기값 할당
number = 20 // 2. 재할당
```
```js
let number = 10 // 1. 선언 및 초기값 할당
let number = 20 // 2. 재선언 불가능
```

### const

- 블록 스코프를 갖는 <span>지역 변수</span>를 선언
- 재할당 불가능 & 재선언 불가능
- 선언과 동시에 초기화 필
```js
const number = 10 // 1. 선언 및 초기값 할당
number = 20 // 2. 재할당 불가능
```
```js
const number = 10 // 1. 선언 및 초기값 할당
const number = 20 // 2. 재선언 불가능
```
```js
const number // const' declarations must be initialized
```


-----


## Data Type

- 원시 자료형 (Primitibe type) : 변수에 값이 직접 저장되는 자료형(불변, 값이 복사)
  + 원시 자료형 - Number, String, Boolean, undefined, null
```js
const bar = 'baz'
console.log(bar) // baz

bar.toUpperCase()
console.log(bar) // baz
```
```js
let a = 10
let b = a
b = 20
console.log(a) // 10
console.log(b) // 20
```

- 참조 자료형 (Reference type) : 객체의 주소가 저장되는 자료형(가변, 주소가 복사)
  + 참조 자료형 - Objects(Object, Array, Function)
```js
const obj1 = { name: 'Alice', age: 30 }
const obj2 = obj1
obj2.age = 40
console.log(obj1.age) // 40
console.log(obj2.age) // 40
```

### 원시 자료형

- Number : 정수 또는 실수형 숫자를 표현하는 자료형
```js
const a = 13
const b = -5
const c = 3.14  // float - 숫자표현
const d = 2.998e9 // 2.998 * 10^8 = 299,800,000
const e = Infinity
const f = -Infinity
const g = NaN // Not a Number를 나타내는 값
```

- String : 정수 또는 실수형 숫자를 표현하는 자료형
```js
const age = 10
const message = `홍길동은 ${age}세입니다.`
console.log(message)
```
> <span>**"Template Literal"**을 사용하여 문자열 사이에 변수 삽입 가능</span>

- null : 변수의 값이 없음을 <span>의도적</span>으로 표현할때 사용
```js
const lastName = null
console.log(lastName) // null
```

- undefined : 변수 선언 이후 직접 값을 할당하지 않으면 <span>자동</span>으로 할당됨
```js
const firstName
console.log(firstName) // undefined
```

- Boolean : true와 false
  + 조건문 또는 반복문에서 boolean이 아닌 데이터 타입은 <span>자동 형변환 규칙</span>에 따라 true 또는 false로 변환됨

|데이터 타입|false|true|
|---|---|---|
|undefined|항상 false|X|
|null|항상 false|X|
|Number|0, -0, NaN|나머지 모든 경우|
|String|빈 문자열|나머지 모든 경우|


-----


## 연산자

- 할당 연산자 : 오른쪽에 있는 피연산자의 평가 결과를 왼쪽 피연산자에 할당하는 연산자
  > =, +=, -=, *=, ++, --

- 비교 연산자 : 피연산자들(숫자, 문자, Boolean 등)을 비교하고 결과값을 ㅂboolean으로 반환하는 연산자
  > <, >

- 동등 연산자 (==) : 두 피연산자가 같은 값으로 평가되는지 비교 후 boolean 값 반환
  + type converter == 

- 일치 연산자 (===) : 두 연산자의 값과 타입이 모두 같은 경우 true를 반환
  + c like ==

- 논리 연산자 - &&, ||, !


-----


## 조건문

- if : 조건 표현식의 결과값을 boolean 타입으로 변환 후 참/거짓을 판단
```js
if (조건문) {
  명령문
} else if (조건문) {
  명령문
} else {
  명령문
}
```


-----


## 반복문

- 종류
  + while
  + for
  + for...in
  + for...of

- while : 조건문이 참이기만 하면 문장을 계속해서 수행
  ```js
  while (조건문) {
    // do something
  }
  ```

- for : 특정한 조건이 거짓으로 판별될 때까지 반복
  ```js
  for ([초기문]; [조건문]; [증감문]) {
    // do something
  }
  ```

- for...in : 객체(object)의 속성을 순회할 때 사용, 속성 이름
  ```js
  for (variable in object) {
    statements
  }
  ```
  ```js
  const fruits = { a: 'apple', b: 'banana' }

  for (const key in fruits) {
    console.log(key) // a, b
    console.log(fruits[key]) // apple, banana
  }
  ```

- for...of : 반복 가능한 객체(배열, 문자열 등)를 순회할 떄 사용, 속성 값
  ```js
  for (variable of object) {
    statements
  }
  ```
  
- for...in vs for...of
```js
const arr = [3, 5, 7]

for (const i in arr) {
  console.log(i) // 0 1 2
}
for (const i of arr) {
  console.log(i) // 3 5 7
}
```
```js
const capitals = {
  korea: '서울',
  france: '파리',
  japan: '도쿄'
}

for (const capital in capitals) {
  console.log(capital) // korea france japan
}
for (const capital in capitals) {
  console.log(capitals[capital]) // 서울 파리 도쿄
}
for (const capital of capitals) {
  console.log(capital)
  // TypeError: capitals is not iterable
}
```


-----


## Tips

- 세미콜론 (semicolon)
  + JS는 세미콜론을 선택적으로 사용 가능
  + 세미콜론이 없으면 ASI<sup><span>Automatic Semicolon Insertion, 자동 세미콜론 삽입 규칙</span></sup>에 의해 자동으로 세미콜론이 삽입됨

- var
  + 재할당 가능 & 재선언 가능
  + ES6 이전에 변수를 선언할 때 사용되던 키워드
  + "호이스팅" 되는 특성으로 인해 예기치 못한 문제 발생 가능
    * -> 따라서 ES6 이후부터는 var 대신 const와 let 사용 권장

- Template literals (템플릿 리터럴)
  + 내장된 표현식을 허용하는 문자열 작성 방식
  + ES6+부터 지원
  + Backtick(``)을 이용하며, 여러 줄에 걸쳐 문자열을 정의할 수도 있고 JS의 변수를 문자열 안에 바로 연결할 수 있는 이점이 생김
  + 표현식은 `$`와 중괄호`${expression}`로 표기
  ```js
  const age = 10
  const message = `홍길동은 ${age}세입니다.`
  ```

- NaN return case
  + 숫자로써 읽을 수 없음 - `Number(undefined)`
  + 결과가 허수 - `Math.sqrt(-1)`
  + 피연산자가 NaN - `7 ** NaN`
  + 정의할 수 없는 계산식 - `0 * Infinity`
  + 문자열을 포함하면서 덧셈이 아님 - `'가' / 3`

- 반복문 내부 const 및 let
  + for문 : 최초 정의한 i 를 재할당 하면서 사용하기 때문에 <span>const 사용시 에러 발생</span>
    > `for (let i = 0; i < arr.length; i++) {...}`
  + for...in, for...of : 재할당이 아니라, 매 반복 시 해당 변수를 <span>새로 정의</span>(재선언 아님)하여 사용하므로 const를 사용해도 에러 발생하지 않음
    