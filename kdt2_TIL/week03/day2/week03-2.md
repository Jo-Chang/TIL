# Week03-2
-   사용자 정의 함수

<br>[Parent Contents...](../../../README.md/#til-today-i-learned)

## Contents
- [Function](#function)
- [return](#return)
- [Input](#input)

---

## Function
-   함수 ( function ) 기본 구조
    +   선언과 호출 ( define & call )
    +   입력 ( Input )
    +   범위 ( Scope )
    +   결과값 ( Output )
-   선언은 `def`를 활용
-   함수명()으로 호출
```
def foo():
    return True

def add(x, y):
    return x + y
```

---

## return
-   함수는 반드시 값 하나만을 return
    -   명시적인 return 없어도 None return
-   return과 동시에 종료

---

## Input
-   Parameter : 함수를 실행할 때, 함수 내부에서 사용되는 식별자
-   Argument  : 함수를 호출 할 때, 넣어주는 값
-   func(*args) - tuple로 처리
-   func(**args) - dictionary로 처리
```
def foo(x, y = 0, z = 1)
...
foo(1, z = 3) # x = 1, y = 0, z = 3
```

---

## Scope
-   scope
    +   global score : 코드 어디에서든 참조 가능
    +   local scopre : 함수가 만든 scope, 함수 내부에서 참조 가능
-   variable
    +   global variable : global scope에 정의된 변수
    +   local variable : local scope에 정의된 변수
```
# 함수 내부에서 글로벌 변수 변경하기
a = 10
def func1():
    global a
    a = 3

print(a)
func1()
print(a)
```