# Python Email

-   파이썬으로 이메일 보내기

<style>
    span { color: #FF5353; }
</style>

## Protocol

-   프로토콜, 통신규약 ( Protocol ) : 컴퓨터, 단말기 등 데이터 통신주체 쌍방간에 원활한 소통을 위해 맺어진 규칙
-   전송방식, 전달방식, 자료의 형식, 코드 변환방식 등 통신에 필요한 다양한 요소의 표준화 규칙을 담고 있음
    +   SMTP ( Simple Mail Transfer Protocol ): 이메일을 보내기(전송) 위한 프로토콜
    +   pop3 ( Post Office Protocol ) : 이메일을 받기(수신) 위한 프로토콜


## Process

1.  smtp 라이브러리 import
```python
import smtplib
```

2. smtp 라이브러리 객체 인스턴스를 생성한다.
```python
my_smtp = smtplib.SMTP_SSL("smtp.gmail.com", 465) 
# SSL ( Secure Sockets Layer ): 보안모드
# 465 - 보안모드 포트 번호

my_smtp = smtplib.SMTP("smtp.gmail.com", 587) ; 
# 비보안모드 
# 587 - 비보안모드 포트 번호
my_smtp.starttls() 
# 암호화 모드 시작(Transfer Layer Security)
```

3. 생성된 인스턴스를 이용하여 로그인한다.
```python
my_smtp.login(id, pwd)
```

4. 메일을 보낸다.
```python
my_smtp.senmail(from주소, to주소, "데이터")
```

5. 객체를 닫는다.
```python
my_smtp.quit()
```

-   Example
```python
import smtplib

my_smtp = smtplib.SMTP_SSL("smtp.gmail.com", 465)
print(my_smtp)

my_smtp.login("testppptestppp", "ppptestppptest")
my_smtp.sendmail("twotwoppp@gmail.com", "twotwoppp@gmail.com", "대한민국".encode("utf-8"))
# 구글은 프로그램을 통해 로그인 하는 것을 막는것이 Default 값이기 때문에
# 구글 로그인 후 보안 설정 변경을 통해 '보안 수준 낮은 앱의 엑세스'를 허용해야함

msg = '''
message ...
...
'''

# 여러명에게 보내기
f_addr="twotwop@gmail.com"
t_addr = ["twotwoppp@gmail.com", "abc@naver.com", "toto@daum.net", "twotwop@daum.net"]
for one_addr in t_addr:
    my_smtp.sendmail(f_addr, one_addr, msg.encode("utf-8"))

print("모든 메일 발송 완료")
my_smtp.quit()
```

## Email Message 객체

-   구조화된 최적화 메시지를 만들기 위한 객체
-   메시지의 템플릿과 같다.
-   smtplib 객체의 send_message() 메서드를 사용하여 템플릿을 날리는 방식
```python
import smtplib
from email.message import EmailMessage

my_smtp = smtplib.SMTP_SSL("smtp.gmail.com", 465) # 465 : 보안 모드 포트 번호
my_smtp.login("testppptestppp@gmail.com", "ppptestppptest")

msg = EmailMessage()
msg['subject'] = "사업안내문"
msg['From'] = "twotwoppp@gmail.com"
msg.set_content("안녕하십니까? ...(중략)...")

for i in range(10): # 메일 10개 한꺼번에 보내기
    msg['To'] = "testppptestppp@gmail.com"
    my_smtp.send_message(msg)
    del msg['To']
print("모두 발송 성공")
```