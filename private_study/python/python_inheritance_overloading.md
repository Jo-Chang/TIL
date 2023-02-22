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
-   class 작성을 통해 재정의 한다.
-   이름 앞뒤에 더블언더스코어(__)가 붙어있다.
>   __init__, __str__, __add__, __lt__ 등

### Magic method 구분

-   연산의 관리
    ```python
    __add__(self,oth)
    __sub__(self,oth)
    __mul__(self,oth)
    ...
    ```
    ```python
    class MyStr(object):
        def __init__(self, string):
            self.string = string
        def __add__(self, string2):
            return self.string + str(string2)

    aa=MyStr("korea")
    bb=aa+590
    print(bb) # korea590
    ```
    ```python
    class MyList(object):
        def __init__(self, data1):
            self.mylist = data1
        def __add__(self, data2):
            new_list = [x+y for x, y in zip(self.mylist, data2.mylist)]

            return new_list

    aa = MyList([3,6,9,12,15])
    bb = MyList([100,200,300,400,500])

    cc = aa+bb  # aa.__add__(bb)
    print(cc)   # [103, 206, 309, 412, 515]
    ```

-   객체의 생성, 초기화, 소멸
    ```python
    __new__(cls[,..])
    __init__(self[,...])
    __del__(self)
    ```

-   객체의 표현
    +   print(), str(), repr() 함수 사용시 호출
    
-   속성 관리
    ```python
    __getattr__(self,name)  # 객체에 존재하지 않는 속성에 참조 시도가 있을 때 호출
    __setattr__(self)       # 객체의 속성 변경 발생시 호출 (재귀호출 주의)
    ```
    ```python
    class Myclass:
        class_name = "Myclass"

        def __getattr__(self, name):
            print(name, " 속성은 없습니다.")

        def __setattr__(self, name, value):
            print(name, " 속성을 ", value, "로 변경요청이 들어왔습니다.")

        def __str__(self):
            return str(Myclass) + "<----클래스명"

    c = Myclass()
    
    print(c.class_name)
    print(c.name)
    print(c.data)
    c.class_name="good class"
    print(c.class_name)
    print(str(c))
    ```

-   디스크립터(Descriptor) 관리
    ```python
    __get__(self, instance, owner)
    __set__(self, instance, value)
    __delete__(self, instance)
    ```
    ```python
    class Descriptor(object):   # 디스크립터 정의
        def __init__(self):
            self.value = ""
        
        def __get__(self, instance, owner):
            print("꺼내오기: %s"%self.value)

        def __set__(self, instance, value):
            print("넣기:%s"%value)
            self.value = value

    class Person(object):   # 소유자(wrapper)
        name = Descriptor()

    pp = Person()   # 사용자
    pp.name="초록빛 바다"
    print("꺼내온 결과-->", pp.name)
    ```
    ```python
    # Descriptor 대신 Decorator 활용
    class sample:
        @property
        def data(self):
            return self.__value
        @data.setter
        def data(self, value):
            print("속성이 변경되었습니다.")
            self.__value = value * 5
        @data.getter
        def data(self):
            print("속성 참조")
            return self.__value

    a = []
    for i in range(5):
        a.append(sample())
        a[i].data = i
    
    for i in range(5):
        print(a[i].data)
    print(a[3].__value)     # AttributeError: "sample object has not attribute "__value"
    # 클래스 내부에서 private 변수 (__value)로 선언했기 때문
    ```

-   컨테이너(집단형 자료, list, tuple, dictionary, ...) 관리
    ```python   
    __len__(self) 
    __getitem__(self, key) 
    __setitem__(self, key, value) 
    __missing__(self, key) 
    __delitem__(self, key)
    __iter__(self)
    __reversed__(self)
    __contains__(self, item)
    ```
    ```python
    class Data(list):
        def __init__(self, data):
            list.__init__(self.data)
            print("초기화")
        def __getitem__(self, key):
            print("getitem호출")
            r = list.__getitem__(self, key)
            return r
        def __setitem__(self, key, data):
            print("setitem호출")
            list.__setitem__(self, key, data)
    
    l = Data([0, 1, 2, 3, 4, 5, 6, 7])  # 초기화
    x = l[5]                            # getitem호출
    l[3] = 33                           # setitem호출
    x = l[3:7]                          # getitem호출
    l[0:4] = [55, 66, 77, 88]           # setitem호출
    l.append(8)                         
    for i in range(len(l)):             
        print(l[i])                     '''
                                        getitem호출
                                        55
                                        getitem호출
                                        66
                                        getitem호출
                                        77
                                        getitem호출
                                        88
                                        getitem호출
                                        5
                                        ...
                                        '''
    ```