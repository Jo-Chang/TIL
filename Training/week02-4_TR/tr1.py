import datetime

while True:
    problem_number = input('문제 번호 입력 > ')
    if problem_number == '1':
        print('# 1. 문자열을 입력 받고 문자열에서 e 의 개수를 구해서 출력하세요.\n\
단, count() 함수는 사용하지마세요.')
        ########## solution code
        str = input('문자열을 입력하세요 > ')
        cnt = 0
        
        for ch in str:
            if ch == 'e':
                cnt += 1
        print(cnt)
        ##########
        print()
        
    elif problem_number == '2':
        print('# 2. 문자열을 입력 받고, 문자열 중 알파벳 모음의 총 개수를 출력하세요.\n\
알파벳 모음 : a(A) e(E) i(I) o(O) u(U)\n단, count() 함수는 사용하지마세요.')
        ########## solution code
        str = input('문자열을 입력하세요 > ')
        cnt = 0
        
        for ch in str:
            if ch == 'a' or ch == 'e' or ch == 'i' or ch =='o' or ch == 'u':
                cnt += 1
            elif ch == 'A' or ch == 'E' or ch == 'I' or ch =='O' or ch == 'U':
                cnt += 1
        print(cnt)
        ##########
        print()
        
    elif problem_number == '3':
        print('# 3. 입력과 같은 딕셔너리 변수가 있을 때, 해당 인물의 나이를 출력하세요.')
        ########## solution code
        dict_variable = {
            "이름": "정우영",
            "생년": "2000",
            "회사": "하이퍼그로스",
        }
        print('나이 :', end = ' ')
        print(f'{datetime.datetime.now().year - int(dict_variable["생년"]) + 1}세')
        ##########
        print()
       
    elif problem_number == '4':
        print('# 4. 이름, 전화번호, 거주지 정보를 입력받아 딕셔너리 구조로 저장하고, 해당 딕셔너리와 딕셔너리의 정보를 구분해서 출력하세요.')
        ########## solution code
        dict_variable = {}
        dict_variable["이름"] = input("이름을 입력하세요 > ")
        dict_variable["전화번호"] = input("전화번호를 입력하세요 > ")
        dict_variable["거주지"] = input("거주지를 입력하세요 > ")
        
        print(dict_variable)
        for key, val in dict_variable.items():
            print(f'{key} : {val}')
        ##########
        print()
        
    elif problem_number == '5':
        print('# 5. 이름, 전화번호, 이메일, 거주지 정보를 입력받아 출력 예시와 동일한 딕셔너리 구조를 출력하세요.\n\
Hint : 딕셔너리 안에 딕셔너리를 넣을 수 있습니다.')
        ########## solution code
        dict_var1 = {}
        dict_var2 = {}
        dict_var1[input('이름을 입력하세요 > ')] = dict_var2
        dict_var2['전화번호'] = input('전화번호를 입력하세요 > ')
        dict_var2['이메일'] = input('이메일을 입력하세요 > ')
        dict_var2['거주지'] = input('거주지를 입력하세요 > ')
        
        print(dict_var1)
        ##########
        print()
        
    elif problem_number == '6':
        print('# 6. 문자열을 입력받고, 문자열에서 개별 문자가 나오는 횟수를 출력하세요.')
        """
        ########## solution code
        str = input('문자열을 입력하세요 > ')
        len = 0
        for ch in str:
            len += 1
        
        for i in range(len):
            for j in range(0, i):
                if str[i] == str[j]:
                    break;
            else:
                count = 0
                for j in range(i, len):
                    if str[i] == str[j]:
                        count += 1
                print(f'{str[i]} {count}')
        ##########
        """
        ########## solution code_use dictionary
        str = input('문자열을 입력하세요 > ')
        dict_var = {}
        for ch in str:
            dict_var[ch] = 0
        
        for ch in str:
            dict_var[ch] += 1
        
        for key, val in dict_var.items():
            print(key, val)
        
        ##########
        print()
       
    else:
        print('Terminated!')
        break