# Python Inheritance & Overloading

-   상속과 메소드 오버로딩

<style>
    span {color: #FF5353;}
</style>


## Inheritance

-   상속 ( Inheritance ) : 어떤 클래스가 다른 클래스로부터 특성과 기능을 물려 받는 것
-   정의되어 있는 데이터 공간이나 메서드 재정의 또는 확장 가능(overriding)
-   코드 재 사용성(code reusability) 증가
-   상속하는 원본 클래스 : base class, super class, parent class
-   상속받아 만들어진 클래스 : Derived class, Sub class, child class

```python
class Car:
    def __init__(self, ...):
        ...
        pass

    def showspec(self):
        ...
        pass

class Truck(car)
    pass

t1 = Truck(...)
t2 = Truck(...)
t1.showspec()
t2.showspec()
```

-   메소드 확장과 치환
```python
class Car:
    def __init__(self, name, weight, size, cylinder):
        ...
        pass

    def showspec(self):
        ...
        pass

class Sedan(Car):
    def __init__(self, name, weight, size, cylinder, color):
        super().__init__(name, weight, size, cylinder)
        # Car.__init__(self, name, weight, size, cylinder)
        self.color = color
    
    def showspec(self):
        super().showspec()
        print(f"색 상 : {self.color}")

class SUV(Sedan):
    pass

s1 = Sedan("소나타", 1.6, 1.9, 2600, "blue")
s1.showspec()
```