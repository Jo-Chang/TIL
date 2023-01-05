# Python File I/O

### open / close
-  open() : file을 열고 읽고 쓰거나, 생성 ( 파일명 존재한다면 내용 덮씌움 )

### write
-   .write() : 파일을 쓰거나 생성

### read
-   .read() : 파일을 읽음

### add
-   'a' 모드로 파일 열고 .write()로 내용 추가

### 예제
```
# w: 쓰기
f = open('C:/~.../{file name}, 'w')

students = ['김철수', '최영', '한석규', '김태희']
for student in students:
    msg = student
    f.write(msg + "\n")

f.close()
```
=
```
# w: 쓰기
students = ['김철수', '최영', '한석규', '김태희']
with open('C:/~.../{file name}, 'w') as f:
    for student in students:
        msg = student
        f.write(msg + "\n")
```

---

```
# r: 읽기 1 -한줄씩 가져옴
f = open('C:/~.../{file name}, 'r')

while True:
    line = f.readline()
    if not line:
        break
    print(line)

f.close()
```
```
# r: 읽기 2 - 한줄씩 List 형태로 가져옴
f = open('C:/~.../{file name}, 'r')

lines = f.readlines()
print(lines)            # ['김철수\n', '최영\n', '한석규\n', '김태희\n']
print(type(lines))      # <class 'list'>
for line in lines:
    print(line)
f.close()
```
```
# r: 읽기 3 - 내용 전체 다 가져옴
f = open('C:/~.../{file name}, 'r')

memo = f.read()
print(memo)
f.close()
```

---

```
# a: 추가
with open('C:/~.../{file name}, 'a') as f:
    f.write('추가인원 : hongku')
```