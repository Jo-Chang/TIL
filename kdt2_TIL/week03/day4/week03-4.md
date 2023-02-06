# Sample_md
-   Class

<br>[Parent Contents...](../../README.md/#til-today-i-learned)

## Contents
- [Attribute](#attribute)
- [Class method](#class-method)
- [Static method](#static-method)
- [Method Summary](#method-summary)
- [Inheritance](#Inheritance)
- [Syntax sugar](#syntax-sugar)
- [tips](#tips)

---

## Attribute
-   클래스 속성 ( attribute ) : 한 클래스의 모든 인스턴스라도 똑같은 값을 가지고 있는 속성
-   클래스 선언 내부에서 정의
-   <classname>.<name>으로 접근 및 할당
```python
class circle:
    pi = 3.14
```

---

## Class Method
-   클래스 메소드 ( method ) : 클래스가 사용할 메소드
-   @classmethod 데코레이터[^1]를 사용하여 정의
-   호출시 첫번째 인자로 클래스(cls)가 전달
```python
class MyClass

    @classmethod
    def clasS_method(cls, arg1, ...)
```

[^1]: 함수를 어떤 함수로 꾸며서 새로운 기능 부여

---

## Static method
-   인스턴스나 클래스를 사용하지 않는 메소드
-   @staticmethod 데코레이터를 사용하여 정의
-   호출시 어떠한 인자도 전달되지 않음
```python
class MyClass

    @staticmethod
    def class_method(arg1, ...)
```

---

## Method Summary
|메소드 이름 | Require |
| --- | --- |
|스태틱 메소드|인스턴스나 클래스를 활용하거나 조작하지 않는 경우, 전달 되는 인자 없음|
|인스턴스 메소드|인스턴스를 활용하거나 조작하는 경우, 첫번째 인자로 전달된 인스턴스를 조작(self)|
|클래스 메소드|클래스를 활용하거나 조작하는 경우, 첫번쨰 인자로 전달된 클래스를 조작(cls)|

---

## Inheritance
-   상속 ( Inheritance ) : 두 클래스 사이 부모 - 자식 관계를 정립하는 것
-   부모에 정의된 속성이나 메소드를 활용하거나 Overriding(재정의)하여 활용
-   `super()` : 자식클래스에서 부모클래스 사용하고 싶을 때 활용
-   Method Overriding
```python
# 부모 클래스 - Person
class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"반갑습니다. {self.name}입니다.")

# 자식 클래스 - Professor
class Professor(Person):
    def talk(self):
        print(f"{self.name}일세.")

# 자식 클래스 - Student
class Student(Person):
    super().talk()
    print("저는 학생입니다.")
```

```python
class Person:
    def __init__(self, name):
        self.name = name

    def greeting(self):
        return f"안녕, {self.name}"

class Mom(Person):
    gene = "XX"

    def swin(self):
        return "엄마가 수영"

class Dad(Person):
    gene = "XY"

    def walk(self):
        return "아빠가 걷기"

class FirstChild(Dad, Mom):
    def swin(self):
        return "첫째가 수영"
    
    def cry(self):
        return "첫째가 응애"

baby1 = FirstChild("아가")
baby1.cry()
# "첫째가 응애"
baby1.swim()
# "첫째가 수영"
baby1.walk()
# "아빠가 걷기"
bay1.gene
# "XY"
```

---

## Syntax sugar
-  조건표현식 ( Conditional Expression )
    ```python
    <true인 경우 값> if <expression> else <false인 경우 값>
    ```
-   enumerate() : 인덱스와 객체를 쌍으로 담은 열거형(enumerate) 객체 반환
    ```python
    members = ["민수", "영희", "철수"]

    for i in range(len(members)):
        print(f"{i} {members[i]}")
        
    for i, member in enumerate(members):
        print(i, member)
    ```
-   List Comprehension
    ```python
    [<expression for <변수> in <iterable>]
    [<expression for <변수> in <iterable> if <조건식>]
    ```
-   Dictionary Comprehension
    ```python
    {key: value for <변수> in <iterable>}
    {key: value for <변수> in <iterable> if <조건식>}
    ```
-   lambda [parameter] : 표현식
    - 표현식을 계산한 결과값을 반환하는 함수, 이름이 없는 함수여서 <span style="color: #2D3748; background-color:#fff5b1;">**익명함수**</span>라고도 불림

-   Type annotation : Type에 대한 설명을 붙임
    ```python
    hello: str = "hello world!"

    def add(x: int, y: int) -> int:
        return x + y

    result: int = add(7, 4)
    ```

-   Positional-only parameters : 함수를 정의할 때 어떻게 호출해야 하는지를 함께 지정
    ```python
    def f(a, b, /, c, d, *, e, f):
        print(a, b, c, d, e, f)
    ```

---

## tips
-   모듈 설치 확인
```shell
c:\>pip freeze
```
>   ref) https://www.zinnunkebi.com/python-modulenotfounderror-requests/