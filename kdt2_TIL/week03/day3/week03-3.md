# Week03-3
-   사용자 정의 클래스, OOP

<br>[Parent Contents...](../../../README.md/#til-today-i-learned)

## Contents
- [object](#object)
- [OOP](#oop)
- [class & instance](#class--instance)
- [method](#method)

---

## object
-   객체 ( object ) : 특정 타입의 인스턴스(instance)[^1]
    > ex) 123, 900, 5는 모두 int의 인스턴스..
-   타입 ( type ) : 어떤 상태(data) 를 가지는가?
-   조작법 ( method ) : 어떤 행위(function)를 할 수 있는가?
-   객체 비교하기
    ```python
    a = [1, 2, 3]
    b = [1, 2, 3]

    print(a == b, a is b)
    # True False
    ```
    ```python
    a = [1, 2, 3]
    b = a

    print(a == b, a is b)
    # True True
    ```
---

## OOP
-   객체 지향 프로그래밍 ( Object Oriented Programming )
: 컴퓨터 프로그램을 여러 개의 독립된 단위, "객체"들의 모임으로 파악하고자 하는 것
-   타입(종류)과 값(실제 사례)
```python
class Rectangle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def area(self):
        return self.x * self.y

    def circumference(self):
        return 2 * (self.x + self.y)
```
```python
r1 = Rectangle(10, 30)
r1.area()
r1.circumference()

r2 = Rectangle(300, 20)
r2.area()
r2.circumference()
```

---

## class & instance
-   클래스 ( class ) : 객체들의 분류
-   인스턴스 ( instance ) : 하나하나의 실체
-   속성 : 특정 데이터 타입, 클래스의 객체들이 가지게 될 데이터
-   self : 인스턴스 자기자신, 파이썬에서 인스턴스 메소드는 호출 시 첫번째 인자로 인스턴스 자신이 전달되게 설계
---

## method
-   메소드 ( method ) : 특정 데이터 타입/클래스의 객체에 공통적으로 적용 가능한 행위(함수)
-   constructor : 인스턴스 객체 생성시 자동으로 호출되는 메소드
    ```python
    class Person:
        
        def __init__(self, name):
            self.name = name # 인스턴스 변수 정의
    ```
-   destructor : 인스턴스 객체가 소멸(파괴)되기 직전에 호출되는 메소드
    ```python
    class Person:

        def __del__(self):
            print('인스턴스가 사라졌습니다.')
    ```
-   magic method : Double underscore(__)가 있는 특수한 동작을 위한 메소드, special method라고도 불림
    > \_\_str__(self), \_\_len__(self), \_\_repr__(self)
    > <br>\_\_lt__(self, other), \_\_le__(self, other), \_\_eq__(self, other)
    > <br>\_\_gt__(self, other), \_\_ge__(self, other), \_\_ne__(self, other)
    +   \_\_str__ : 해당 객체의 출력 형태를 지정, 프린트 함수 호출 시 자동 호출
    +   \_\_gt__ : 부등호 연산자(>, greater than)
    ```python
    class Circle:

        def __init__(self, r):
            self.r = r
        
        def area(self):
            return 3.14 * self.r * self.r

        def __str__(self):
            return f'[원] radius: {self.r}'
        
        def __gt__(self, other):
            return self.r > other.r
    ```
    ```python
    c1 = Circle(10)
    c2 = Circle(1)

    print(c1)
    # [원] radius: 10
    print(c2)
    # [원] radius: 1

    c1 > c2
    # True
    c1 < c2
    # False
    ```