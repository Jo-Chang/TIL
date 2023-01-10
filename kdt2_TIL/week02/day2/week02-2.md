# Week02-2
-   제어문

<br>[Parent Contents...](../../../README.md/#til-today-i-learned)

## Contents
- [String Formatting](#string-formatting)
- [형변환](#형변환--typecasting)
    + [암시적 형변환](#암시적-형변환--implicit)
    + [명시적 형변환](#명시적-형변환--explicit)
* [*문자열 출력 tip](#문자열-출력-tip)
- [제어문](#제어문)
    + [조건문](#조건문)
    + [반복문](#반복문)
    + [반복문 제어](#반복문-제어)

---

## String Formatting
-   문자열을 변수를 활용하여 만들기
```
name = 'Kim'
score = 4.5

print('Hello, %s' % name)
print('내 성적은 %d' % score)
print('내 성적은 %f' % score)

# Hello, Kim
# 내 성적은 4
# 내 성적은 4.5
```
---

## 형변환 ( Typecasting )
-   In python, 데이터 형태 서로 변환 가능

### 암시적 형변환 ( Implicit ) 
-   사용자가 의도하지 않은 형 변환

### 명시적 형변환 ( Explicit )
-   사용자가 특정 함수를 활용하여 의도하여 형 변환

#### *문자열 출력 tip
```
print('이름 : ' + name + ', 나이 : ' + str(age))
print('이름 : {}, 나이 : {}'.format(name, age))
print(f'이름 : {name}, 나이 : {age}')
```

---

## 제어문
-   객체를 제어
-   특정 상황에 따라 코드를 선택적, 반복적으로 실행
-   순서도 ( flow chart ) 활용 표현
-   조건문, 반복문, ...

---

### 조건문
-   참/거짓 판단하는 조건식 사용
-   if와 else를 활용
```
if < expression > :
    # Run this Code block
else:
    # Run this Code block
```

### 복수 조건문
-   elif를 활용

### 중첩 조건문
-   if문 안 if문

<a name = "range"></a>
#### * range()
-   숫자의 시퀀스를 나타내기 위해 사용
-   기본형 : range(n)
    -   0 ~ n-1
-   범위 지정 : range(n, m)
    -   n ~ m-1
```
a = range(4)
print(a)        # range(0, 4)
print(list(a))  # [0, 1, 2, 3]

b = range(0, -6, -1)
print(b)        # range(0, -6, -1)
print(list(b))  # [0, -1, -2, -3, -4, -5]
```

---

### 반복문
-   특정 조건을 도달할 때까지, 계속 반복되는 일련의 문장
>   keyword) while 문 / for 문 / 반복 제어

#### for문
-   시퀸스(string, tuple, list, range)를 포함한
```
a = 'apple'
for char in a:
    print(char)
#   a
    p
    p
    l
    e

list = ['윤원', '용진', '필진']
for name in list:
    print(name)
#   윤원
    용진
    필진

for num in range(3):
    print(num**2)
#   0
    1
    4

chars = input()
for idx in range(len(chars)):
    print(chars[idx])
```

---

### 반복문 제어

-   break :
    반복 즉시 종료
-   continue :
    continue 이후는 수행하지 않고 다음 반복
-   for-else : 
    for 문이 다 수행되고 난 이후에 break 되지 않았다면 수행

---