# Python excel-email training

import smtplib
import openpyxl
from email.message import EmailMessage

str1 = ''' str1...
'''
str2 = ''' str2...
'''
str3 = ''' str3...
'''

msg_source = (str1, str2, str3) # 튜플로 만든다

#---메일 오픈
my_smtp = smtplib.SMTP("smtp.gmail.com", 587)   
my_smtp.starttls()  # 비보안모드
my_smtp.login("testppptestppp", "mypwd")

#---엑셀 오픈
wb = openpyxl.load_workbook("test2.xlsx")
sh = wb.active

msg = EmailMessage()
msg['Subject'] = " 응시결과 안내문 "
msg['From'] = "twotwoppp@gmail.com"

for o_row in sh.rows:
    u_name = o_row[0].value # 고객명
    u_mail = o_row[3].value # 고객메일주소
    u_pass = o_row[4].value # 합불여부
    
    msg['To'] = u_mail
    
    if u_pass == 'p':
        msg_point = 0
        
    elif u_pass == 'f':
        msg_point = 1
    
    else:
        msg_point = 2
        
    mymsg = u_name + msg_source(msg_point)
    msg.set_content(mymsg)  # 조합된 것 넣기
    my_smtp.send_message(msg)   # 전송한다.
    print(mymsg)
    del msg['To']       # 새로운 것 넣기 위해 삭제
    msg.clear_content() # 새로운 것 넣기 위해 삭제 