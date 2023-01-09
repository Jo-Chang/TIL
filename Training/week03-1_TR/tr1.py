while True:
    problem_number = input('문제 번호 입력 > ')
    if problem_number == '1':
        print(f'# {problem_number}. ')
        ########## solution code
        num = int(input('정수를 입력하세요 > '))
        
        print(num)
        ##########
        print()
        
    elif problem_number == '2' or problem_number == '6':
        print(f'# {problem_number}. ')
        ########## solution code
        n1, n2 = list(map(int, input().split()))

        print(n1, n2)
        ##########
        print()
        
    elif problem_number == '3' or problem_number == '5' \
        or problem_number == '8' or problem_number == '9':
        print(f'# {problem_number}. ')
        ########## solution code
        nums = list(map(int, input().split()))

        for n in nums:
            print(n, end = ' ')
        print()
        # print(*nums)
        # * : 언패킹 ( unpacking )
        ##########
        print()
       
    elif problem_number == '4' or problem_number == '7':
        print(f'# {problem_number}. ')
        ########## solution code
        strings = input().split()

        print(*strings)
        ##########
        print()
        
    else:
        print('Terminated!')
        break