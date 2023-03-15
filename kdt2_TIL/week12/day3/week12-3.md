# Week12-3

-   JavaScript - Functions, Object, Array


<link rel="stylesheet" href="../../assets/stylesheets/my_style.css">

<br>[Parent Contents...](../../README.md/#til-today-i-learned)

## Contents
- [참조 자료형](#참조-자료형)
- [Function](#function)
- [Object](#object)
  + [Method](#object-method)
- [Array](#array)
  + [Method](#array-method)
  + [Short Conclusion](#배열-정리)
- [Tips](#tips)

<br>


-----


## 참조 자료형

- 참조 자료형 ( Reference type ) : Objects (Object, Array, Function)


-----


## Function

- Function : 참조 자료형, 모든 함수는 Function object

- 함수(Function)의 구조
  + 함수의 이름
  + 함수의 매개변수
  + 함수의 body를 구성하는 statement
  ```js
  function name ([param[, param,[..., param]]]) {
    statements
    return value  // return이 없다면 undefined 반환
  }
  ```

- 함수의 정의
  + 선언식 ( Declaration )
  ```js
  function funcName () {
    statements
  }
  ```
  + 표현식 ( Expression )
  ```js
  const funcName = function () { // 익명함수 (lambda, void) 사용법
    statements
  }
  ```

- 기본 함수 매개변수 - 값이 없거나 undefined가 전달된 경우 이름 붙은 매개변수를 기본값으로 초기화
  ```js
  const greeting = function (name = 'Anonymous') {
    return `Hi ${name}`
  }

  greeting() // Hi Anonymous
  ```

- 매개변수와 인자의 개수 불일치
  ```js
  const noArgs = function () {
    return 0
  }
  noArgs(1, 2, 3) // 0

  const twoArgs = function (arg1, arg2) {
    return [arg1, arg2]
  }
  twoArgs(1, 2, 3)  // [1, 2]
  ```
  ```js
  const threeArgs = function (arg1, arg2, arg3) {
    return [arg1, arg2, arg3]
  }

  threeArgs() //  [undefined, undefined, undefined]
  threeArgs(1)  //  [1, undefined, undefined]
  threeArgs(2, 3) // [2, 3, undefined]
  ```

- 나머지 매개변수 ( Rest Parameters ) : 무한한 수의 인자를 '배열'로 허용하여 가변 함수를 나타내는 방법
  ```js
  const myFunc = function (arg1, arg2, ...restArgs) {
    return [arg1, arg2, ..., restArgs]
  }

  myFunc(1, 2, 3, 4, 5) // [1, 2, [3, 4, 5]]
  myFunc(1, 2)  // [1, 2, []]
  ```

- 화살표 함수 표현식 ( Arrow function expressions ) : 함수 표현식의 간결한 표현법
  ```js
  const arrow11 = function (name) {
    return `heelo, ${name}`
  }

  // 1. function 키워드 삭제 후 화살표 작성
  const arrow2 = (name) => { return `hello, ${name}` }

  // 2. 인자가 1개일 경우에만 () 생략 가능
  const arrow3 = name => { return `hello, ${name}` }

  // 3. 함수 바디가 return을 포함한 표현식 1개일 경우에 {} & return 삭제 가능
  const arrow4 = name => `hello, ${name}`
  ```

- 화살표 함수 표현식 응용
  ```js
  // 1. 인자가 없다면 () or _ 로 표시 가능
  const noArgs1 = () => 'No args'
  const noArgs2 = _ => 'No args'

  // 2-1. object를 return 한다면 return 을 명시적으로 작성해야 함
  const returnObject1 = () => { return { key: 'value'}}

  // 2-2. return을 적지 않으려면 소괄호로 감싸야 함
  const returnObject2 = () => ({ key: 'value' })
  ```


-----


## Object

- Object : 키로 구분된 데이터 집합(data collection)을 저장하는 자료형<sup><span>plain object</span></sup>
- 객체의 구조
  + 중괄호를 이용해 작성
  + 중괄호 안에는 key: value 쌍으로 구성된 속성(property)를 여러 개 넣을 수 있음
  + key는 문자형, value는 모든 자료형이 허용
  ```js
  const user = {
    name: 'Sophia',
    age: 30,
    'key with space': true, // "trailing comma" - 속성을 추가, 삭제, 이동하기가 용이해짐
  }
  ```

- Property 활용 ( CRUD )
  ```js
  // 조회
  console.log(user.age) // 30
  console.log(user['key with space']) // true

  // 추가
  user.address = 'korea'
  console.log(user) // {name: 'Sophia', age: 30, key with space: true, address: 'korea'}

  // 수정
  user.age = 20
  console.log(user.age) // 20

  // 삭제
  delete user.address
  console.log(user) // {name: 'Sophia', age: 20, key with space: true}

  // 존재 여부 확인 - "in"
  console.log('age'in user) // true
  console.log('coutry' in user) //false
  ```

- Property 단축 : 키 이름과 값으로 쓰이는 변수의 이름이 같은 경우 단축 구문 사용 가능
  ```js
  const age = 30
  const address = 'korea'

  const oldUser = {
    age: age,
    address: address,
  }

  const newUser = {
    age,
    address,
  }
  ```

- 계산 Property : 키가 대괄호([])로 둘러싸여 있음, 고정된 값이 안닌 변수 값 사용 가능
  ```js
  const product = prompt('물건 이름을 입력하세요.')
  const prefix = 'my'
  const suffix = 'property'

  const bag = {
    [product]: 5,
    [prefix + suffix]: 'value',
  }

  console.log(bag)  // {연필: 5, myproperty: 'value'}
  ```

### Object Method

- Method : 객체 속성에 정의된 함수
  + <span>'this'</span> 키워드를 사용해 객체에 대한 특정한 작업을 수행할 수 있음
  + 객체를 <span>행동</span> 할수 있게 함
  ```js
  const person = {
    name: 'Sophia',
    greeting: function () {
      return `Hello my name is ${this.name}`
    },
  }

  console.log(person.greeting())  // Hello my name is Sophia
  ```

- `'this'` keyword : function이나 method를 호출한 객체를 가리키는 키워드
  + 함수 내에서 객체의 속성 및 method에 접근하기 위해 사용

- JavaScript에서 `this`는 호출하는 방법에 따라 지시 대상 다름
  + 단순 호출 -> 전역 객체
    ```js
    const myFunc = function () {
      return this
    }

    console.log(myFunc()) // window
    ```
  + method 호출 -> method 호출 객체
    ```js
    const myObj = {
      data: 1,
      myFunc: function () {
        return this
      }
    }

    console.log(myObj.myFunc()) // myObj
    ```

- Nested 함수에서의 문제점
  ```js
  // Nested 함수에서의 문제점
  const myObj2 = {
    numbers: [1, 2, 3],
    myFunc: function () {
      this.numbers.forEach(function (number) {
        console.log(number) // 1 2 3
        console.log(this) // window
      })
    }
  }
  ```
  ```js
  const myObj3 = {
    numbers: [1, 2, 3],
    myFunc: function() {
      this.numbers.forEach((number) => {
        console.log(number) // 1 2 3
        console.log(this) // myObj3
      })
    }
  }
  ```


-----


## Array

- 배열 ( Array ) : 순서가 있는 데이터 집합 (data collection)을 저장하는 자료구조
- 배열의 구조
  + 대괄호를 이용해 작성
  + length를 사용해 배열에 담긴 요소 갯수
  + 배열 요소의 자료형엔 제약이 없음
  + 배열의 마지막 요소는 객체와 마찬가지로 <span>trailing comma</span> 가능
  ```js
  const fruits = ['apple', 'banana', 'coconut']

  console.log(fruits[0])
  console.log(fruits[1])
  console.log(fruits[2])

  console.log(fruits.length)
  ```

- 배열과 반복
  ```js
  // for
  for (let i = 0; i < fruits.length; i++) {
    console.log(fruits[i])
  }

  // for...of
  for (const fruit of fruits) {
    console.log(fruit)
  }
  ```

### Array Method

|Method|기능|역할|
|---|---|---|
|push / pop|배열 끝(오른쪽) 요소를 추가 또는 제거|요소 추가/제거|
|unshift / shift|배열 앞(왼쪽) 요소를 추가 또는 제거|요소 추가/제거|
|forEach|인자로 주어진 함수(콜백함수)를 배열 요소 각각에 대해 실행|반복|
|map|배열 요소 전체를 대상으로 함수(콜백함수)를 호출하고, <br>함수 호출 결과를 배열로 반환|변형|

- push / pop / unshift / shift - **Deque**의 append / pop / appendleft / popleft와 동일

- forEach : 인자로 주어진 함수<sup>콜백 함수</sup>를 배열 요소 각각에 대해 실행
  + 3가지 매개변수로 구성
    * item: 배열의 요소
    * index: 배열 요소의 인덱스
    * array: 배열
  + 반환값: undefined
  ```js
  array.forEach(function (item, index, array) {
    // do something
  })
  ```

- 콜백 함수 ( Callback function ) : 다른 함수에 인자로 전달되는 함수
  + 외부 함수내에서 호출되어 일종의 루틴이나 특정 작업을 진행

- map : 배열 요소 전체를 대상으로 함수<sup>콜백 함수</sup>를 호출하고, 함수 호출 결과를 모아 <span>새로운 배열을 반환</span>
  + 기본적으로 forEach와 같지만, forEach와 달리 새로운 배열을 반환
  ```js
  const result = array.map(function (item, index, array) {
    // do something
  })
  ```

### 배열 정리

- 배열의 본질은 객체
- 배열의 요소를 대괄호 접근법을 사용해 접근하는 건 사실 객체 문법과 같음 ( Key를 숫자로 사용 )
- 숫자형 키를 사용함으로써 배열은 객체 기본 기능 이외에도 순서가 있는 컬렉션을 제어하게 해주는 특별한 메서드 제공


-----


## Tips

- 객체 메서드 Object
  ```js
  const profile = {
    name: 'Sophia',
    age: 30,
  }

  console.log(Object.keys(profile)) // ['name', 'age']
  console.log(Object.values(profile)) // ['Sophia', 30]
  ```

- JS 'this' 특징
  + 함수가 <span>호출되는 방식</span>에 따라 결정되는 현재 객체
  + Python의 self와 Java의 this는 선언시 값이 이미 정해짐,
  이와 다르게 함수 호출전까진 값이 할당되지 않고 호출시에 결정됨 (동적)

- JSON (JavaScript Object Notation)
  + Key-Value 형태로 이루어진 자료 표기법
  + JS의 Object와 유사한 구조지만, JSON은 형식이 있는 <span>문자열</span>
  + JS에서 JSON을 사용하기 위해서는 Object 자료형으로 변경해야 함
  ```js
  const jsObject = {
    coffee: 'Americano'
    iceCream: 'Cookie and cream',
  }
  ```
  ```js
  // Object -> JSON

  const objToJson = JSON.stringify(jsObject)

  console.log(objToJson)  // {"coffee":"Americano", "iceCream":"Cookie and cream"}
  console.log(typeof objToJson) // string
  ```
  ```js
  // JSON -> Object

  const jsonToObj = JSON.parse(objToJSON)

  console.log(jsonToObj)  // { coffee: 'Americano', iceCream: 'Cookie and cream'}
  console.log(typeof jsonToObj) // object
  ```

- 배열 순회

  | 방식 | 특징 | 비고 | 
  | --- | --- | --- | 
  | for | 배열의 index 이용하여 각 요소 접근 <br>break, continue 사용 가능 |  | 
  | for...of | 배열 요소에 바로 접근 <br>break, continue 사용 가능 |  | 
  | forEach | 간결하고 가독성 높음, callback함수를 이용하여 각 요소 조작 용이 <br>break, continue 사용 불가능 | 사용 권장 | 

- 콜백 함수 사용 이유
  + 재사용성
  + 가독성
  + 비동기적 처리
    ```js
    console.log('a')

    setTimeout(() => {  // n 시간 이후 실행
      console.log('b')
    }, 3000)  // 1초 = 1000

    console.log('c')

    // Result : a c b
    ```