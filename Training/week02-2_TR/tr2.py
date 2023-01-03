while True:
    num = input('문제 번호 입력 > ')
    if num == '1':
        print('# 1. 정수 한 개를 입력 받고, 해당 숫자가 0보다 큰 숫자라면 True 아니면 False를 출력하세요.')
        ### solution code
        num1 = int(input('정수를 입력하세요 > '))
        
        if num1 > 0:
            print(True)
        else:
            print(False)
        ###
        print()

    elif num == '2':
        print('# 2. 정수 두 개를 입력 받고, 크기가 더 큰 정수를 출력하세요. 두 정수가 같으면 False를 출력하세요.')
        ### solution code
        num2_1 = int(input('첫 번째 정수를 입력하세요 > '))
        num2_2 = int(input('두 번째 정수를 입력하세요 > '))
        
        if num2_1 > num2_2:
            print(num2_1)
        elif num2_1 < num2_2:
            print(num2_2)
        else:
            print(False)
        ###
        print()

    elif num == '3':
        print('# 3. 정수 한 개를 입력 받고, 해당 정수가 1 보다 크고, 10보다 작다면 True 아니면 False를 출력하세요.')
        ### solution code
        num3 = int(input('정수를 입력하세요 > '))
        
        if num3 > 1:
            if num3 < 10:
                print(True)
            else:
                print(False)
        else:
            print(False)
        ###
        print()

    elif num == '4':
        print('# 4. 정수 한 개를 입력 받고 0 보다 크고, 짝수라면 True 아니면 False를 출력하세요.')
        ### solution code
        num4 = int(input('정수를 입력하세요 > '))
        
        if num4 > 0 and num4 % 2 == 0:
            print(True)
        else:
            print(False)
        ###
        print()

    elif num == '5':
        print('# 5. 정수 한 개를 입력 받고, 아래 조건에 따라 출력하세요.')
        print(' - 값이 100 초과 / 0 미만이면 "에러" 출력')
        print(' - 값이 60 이상이면 "합격" 출력')
        print(' - 값이 60 미만이면 "불합격" 출력')
        ### solution code
        num5 = int(input('정수를 입력하세요 > '))
        
        if num5 < 0:
            print('에러')
        elif num5 < 60:
            print('불합격')
        elif num5 <= 100:
            print('합격')
        else:
            print('에러')
        ###
        print()

    elif num == '6':
        print('# 6. 문자열을 입력 받고, 입력 받은 문자열을 반대로 한 글자씩 출력하세요.')
        ### solution code
        str6 = input('문자열을 입력하세요 > ')
        len = len(str6)
        
        # for i in range(len):
        #    print(str6[len - i - 1])
        for i in range(len, 0, -1):
           print(str6[i - 1])
        ###
        print()

    elif num == '7':
        print('# 7. 정수 두 개를 입력 받고, 두 수 사이의 정수를 오름차순으로 출력하세요.')
        print('두 값이 같으면 False를 출력하세요.')
        ### solution code
        num7_1 = int(input('첫 번째 정수를 입력하세요 > '))
        num7_2 = int(input('두 번째 정수를 입력하세요 > '))
        
        if num7_1 > num7_2:
            for i in range(num7_2 + 1, num7_1):
                print(i)
        elif num7_1 < num7_2:
            for i in range(num7_1 + 1, num7_2):
                print(i)
        else:
            print(False)
        ###
        print()

    elif num == '8':
        print('# 8. 정수 두 개를 입력 받고, 두 수 사이의 정수를 내림차순으로 한 줄에 모두 출력하세요.')
        print('두 값이 같으면 False를 출력하세요')
        ### solution code
        num8_1 = int(input('첫 번째 정수를 입력하세요 > '))
        num8_2 = int(input('두 번째 정수를 입력하세요 > '))
        
        if num8_1 < num8_2:
            for i in range(num8_2 - 1, num8_1, -1):
                print(i, end = ' ')
        elif num8_1 > num8_2:
            for i in range(num8_1 - 1, num8_2, -1):
                print(i, end = ' ')
        else:
            print(False)
        ###
        print()

    elif num == '9':
        print('# 9.정수 한 개를 입력 받고, 1 부터 입력 값 사이의 정수 중 홀수만 출력하세요.')
        print('입력 값이 1보다 작으면 False를 출력하세요.')
        ### solution code
        num9 = int(input('정수를 입력하세요 > '))
        
        if num9 < 1:
            print(False)
        else:
            for i in range(num9):
                if i % 2 == 1:
                    print(i)
        ###
        print('hello')

    elif num == '10':
        print('# 10. 구구단을 출력하세요.')
        print(' - 반복')
        ### solution code
        for i in range(2, 10):
            for j in range(2, 10):
                print(f'{i} X {j} = {i * j}')
        ###
        print()
        
    else:
        print('End!')
        break