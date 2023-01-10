while True:
    problem_number = input('문제 번호 입력 > ')
    if problem_number == '1':
        print(f'# {problem_number}. 정수를 출력하세요.')
        ########## solution code
        print(int(input()))
        ##########
        print()
        
    elif problem_number == '2':
        print(f'# {problem_number}. 단어를 구분해서 출력하세요.')
        ########## solution code
        words = input().split()
        for word in words:
            print(word, end = ' ')
        print()
        ##########
        print()
        
    elif problem_number == '3':
        print(f'# {problem_number}. 테스트 케이스마다 입력 값을 그대로 출력하세요.')
        ########## solution code
        testcase = int(input())
        for i in range(testcase):
            print(input())
        ##########
        print()
       
    elif problem_number == '4':
        print(f'# {problem_number}. 2개 이상의 정수를 출력하세요.')
        ########## solution code
        numbers = list(map(int, input().split()))
        
        for num in numbers:
            print(num, end = ' ')
        print()
        ##########
        print()
        
    elif problem_number == '5':
        print(f'# {problem_number}. 2개의 정수를 출력하세요.')
        ########## solution code
        n1, n2 = list(map(int, input().split()))
        print(n1, n2, sep = ' ')
        ##########
        print()
        
    elif problem_number == '6':
        print(f'# {problem_number}. 단어를 구분해서 출력하세요.')
        ########## solution code
        words = input().split()
        for word in words:
            print(word, end = ' ')
        ##########
        print()
       
    elif problem_number == '7':
        print(f'# {problem_number}. 테스트 케이스마다 입력 값을 그대로 출력하세요.')
        ########## solution code
        T = int(input())
        
        for i in range(T):
            print(input())
        ##########
        print()
        
    elif problem_number == '8':
        print(f'# {problem_number}. 테스트 케이스마다 입력 값을 그대로 출력하세요.')
        ########## solution code
        T = int(input())
        
        for i in range(T):
            print(input())
        ##########
        print()
       
    else:
        print('Terminated!')
        break