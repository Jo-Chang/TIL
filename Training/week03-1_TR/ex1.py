while True:
    problem_number = input('문제 번호 입력 > ')
    if problem_number == '1':
        print('# 1. 5를 입력받아보세요.')
        ########## solution code
        num = int(input('정수를 입력하세요 > '))
        print(num)
        ##########
        print()
        
    elif problem_number == '2':
        print('# 2. 공백으로 구분된 여러개의 정수 입력 받기')
        ########## solution code
        numbers = list(map(int, input("숫자를 입력하세요 > ").split()))

        print(numbers)
        ##########
        print()
        
    elif problem_number == '3':
        print('# 3. 공백으로 구분된 여러개의 단어 입력 받기')
        ########## solution code
        string = input("문자열 입력 > ").split()

        print(string)
        ##########
        print()
       
    elif problem_number == '4':
        print('# 4. 공백으로 구분된 2개의 정수 입력 받기')
        ########## solution code
        a, b = list(map(int, input().split()))

        print(a, b)
        ##########
        print()
       
    else:
        print('Terminated!')
        break