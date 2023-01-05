while True:
    example_number = input('문제 번호 입력 (문제 번호 외 입력시 종료)> ')
    if example_number == '1':
        print('# 1')
        ########## training code
        dict_variable = {}
        dict_variable["이름"] = "정우영"
        dict_variable["생년월일"] = "19000101"
        dict_variable["회사"] = "하이퍼그로스"

        print(dict_variable["이름"]) # 정우영
        print(dict_variable["생년월일"]) # 19000101
        print(dict_variable["회사"]) # 하이퍼그로스
        ##########
        print()
        
    elif example_number == '2':
        print('# 2')
        ########## training code
        dict_variable = {"a": "A", "B": "b"}
        dict_variable["c"] = "C"
        dict_variable["D"] = "d"
        dict_variable["e"] = "E"


        print(dict_variable["a"]) # A
        print(dict_variable["D"]) # d 
        print(dict_variable["b"]) # None ## KeyError
        ##########
        print()
        
    elif example_number == '3':
        print('# 3')
        ########## training code      
        dict_variable = {}
        dict_variable["apple"] = 5000
        dict_variable["banana"] = 3000
        dict_variable["apple"] = 2000
        dict_variable["banana"] = dict_variable["banana"] + 1000

        print(dict_variable["apple"] + dict_variable["banana"]) # 6000
        ##########
        print()
        
    elif example_number == '4':
        print('# 4')
        ########## training code
        dict_variable = {
            "이름": "정우영",
            "생년월일": "19000101",
            "회사": "하이퍼그로스",
        }

        for key in dict_variable:
            print(key, dict_variable[key])

        """
        예측을 작성하세요.
        이름 정우영
        생년월일 19000101
        회사 하이퍼그로스
        """
        ##########
        print()
        
    elif example_number == '5':
        print('# 5')
        ########## training code
        dict_variable = {
            "이름": "정우영",
            "생년월일": "19000101",
            "회사": "하이퍼그로스",
        }

        for key, value in dict_variable.items():
            print(key, value)

        """
        예측을 작성하세요.
        이름 정우영
        생년월일 19000101
        회사 하이퍼그로스
        """
        ##########
        print()
        
    elif example_number == '6':
        print('# 6')
        ########## training code
        dict_variable = {
            "이름": "정우영",
            "생년월일": "19000101",
            "회사": "하이퍼그로스"
        }
        
        print("나이" in dict_variable) # None ## False
        ##########
        print()
        
    elif example_number == '7':
        print('# 7')
        ########## training code
        dict_variable = {
            "이름": "정우영",
            "생년월일": "19000101",
            "회사": "하이퍼그로스",
        }
        
        if "거주지" not in dict_variable:
            dict_variable["거주지"] = "서울특별시"
            # 위 조건문의 조건식이 무엇을 의미하는지 작성하세요.
            # 거주지라는 키값이 dict_variable dictionary 안에 존재하지 않을 경우 참
        
        print(dict_variable) 
        # ["이름": "정우영", "생년월일": "19000101", "회사": "하이퍼그로스", "거주지": "서울특별시"]
        ## # {"이름": "정우영", "생년월일": "19000101", "회사": "하이퍼그로스", "거주지": "서울특별시"}
        ##########
        print()
        
    elif example_number == '8':
        print('# 8')
        ########## training code
        list_variable = []
        
        try:
            list_variable.append(0)
            list_variable.append(1)
            list_variable.append(2)
            print(list_variable[3])
            
        except:
            print("에러가 발생했습니다.")
            print("에러의 원인은 무엇인가요?")
            
        """
        출력 결과를 예측해서 작성하세요.
        에러가 발생했습니다.
        에러의 원인은 무엇인가요?
        A. 리스트에 존재하는 인덱스 외 인덱스를 참조하려고 시도하였으므로 IndexError 발생)
        """
        ##########
        print()
        
    elif example_number == '9':
        print('# 9')
        ########## training code
        try:
            number = 1
            # if number == 1    // try catch로 잡을 수 없는 Syntax Error라 실행가능하게 임시 수정
            if number == 1:
                print(number)
               
                
        except:
            print("에러가 발생했습니다.")
            print("에러의 원인은 무엇인가요?")
        
        """
        에러 원인
        if number == 1 뒤에 :이 누락되었다. -> Syntax Error
        """
        ##########
        print()
        
    elif example_number == '10':
        print('# 10')
        ########## training code
        n = 10
        total = 0
        
        for number in range(0, n + 1):
            if number % 2 == 0:
                total += number * 2
            elif number % 2 == 1:
                total += number + 1 * 3
                
        print(total) # 100
        ##########
        print()
        
    else:
        print('Terminated!')
        break