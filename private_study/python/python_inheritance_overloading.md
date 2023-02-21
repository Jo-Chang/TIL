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

-   클래스 정체성 확인
    +   __bases__
    +   __class__
    +   isinstance()

```python
print(Car.__bases__)            # (<class 'object'>)
print(Car)                      # <class '__main__.Car'>
print(Truck.__bases__)          # (<class '__main__.Car'>,)
print(Truck)                    # <class '__main__.Truck'>
t1 = Truck(...)                 
print(t1)                       # <__main__.Truck object at 0x...>
print(t1.__class__)             # <class '__main__.Truck'>
print(isinstance(t1, Truck))    # True
print(help(Truck))              ''' Help on class Truck in module __main__:
                                    class Truck(Car)
                                    | Truck (name, weight, size, cylinder)
                                    |
                                    | Method resolution order:
                                    | ...
                                    | ...
                                    | ...
                                    None
                                '''
```

-   파이썬 내장클래스 상속
    +   list, dict 등 파이썬 내장클래스를 상속 받아 특정 메서드만 재 정의 해서 사용
```python
class MyDict(dict):

    def keys(self):
        k = super().keys()
        return sorted(k)

    def items(self):
        k = super().items()
        return sorted(k, key=lambda a:a[1])

data = MyDict({
    'japan': 26,
    'china': 28,
    'america': 34,
    'korea': 33
})

print(data.keys())  # ['america', 'china', 'japan', 'korea']
print(data.items()) # [()'japan': 26), ('china': 28), ('america': 34), ('korea': 33)]
for k, v in data.items():
    print(k, v)
    '''
    japan 26
    china 28
    korea 33
    america 34
    '''
```

-   GUI도 상속 가능

## Magic method & Operator Overloading

-   연산자 중복 ( Operator Overloading ) : 언어에서 미리 정의되어 있는 일부 연산자나 메서드의 재정의를 허용하는 것
>   Special method, Magic method, Dunder(__) method