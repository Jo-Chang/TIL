# import copy
while True:
    problem_number = input('문제 번호 입력 > ')
    
    if problem_number == '1':
        print('# 1. 정수 한 개를 입력 받고, 해당 정수의 절대값을 출력하세요.\n\
단, abs() 함수는 사용하지 마세요.')
        ########## solution code
        num = int(input('정수를 입력하세요 > '))
        
        if num < 0:
            num *= -1
        print(num)
        ##########
        print()
        
    elif problem_number == '2':
        print('# 2. 정수만 저장한 리스트가 주어집니다. 리스트 요소의 개수를 출력하세요.\n\
단, len() 함수는 사용하지 마세요')
        ########## solution code
        num_list = list(map(int, input('리스트를 입력하세요 (빈 리스트 입력은 Enter) > ').split()))
        count = 0
        
        for num in num_list:
            count += 1
        print(count)
        ##########
        print()
        
    elif problem_number == '3':
        print('# 3. 정수만 저장한 리스트가 주어집니다. 리스트에 저장된 정수들의 합을 출력하세요.\n\
단, sum() 함수는 사용하지 마세요.')
        ########## solution code
        num_list = list(map(int, input('리스트를 입력하세요 > ').split()))
        sum = 0
        
        for num in num_list:
            sum += num
        print(sum)
        ##########
        print()
       
    elif problem_number == '4':
        print('# 4. 정수만 저장한 리스트가 주어집니다. 리스트에 저장된 정수들의 평균을 출력하세요.\n\
단, len() / sum() 함수는 사용하지 마세요.')
        ########## solution code
        num_list = list(map(int, input('리스트를 입력하세요 > ').split()))
        sum = 0
        count = 0
        
        for num in num_list:
            sum += num
            count += 1
        print(sum / count)
        ##########
        print()
        
    elif problem_number == '5':
        print('# 5. 정수만 저장한 리스트가 주어집니다. 리스트에 저장된 정수들의 곱을 출력하세요.')
        ########## solution code
        num_list = list(map(int, input('리스트를 입력하세요 > ').split()))
        product = 1
        
        for num in num_list:
            product *= num
        print(product)
        ##########
        print()
        
    elif problem_number == '6':
        print('# 6. 양의 정수만 저장한 리스트가 주어집니다. 리스트에 저장된 정수 중 가장 큰 값을 출력하세요.\n\
단, max() 함수는 사용하지 마세요.')
        ########## solution code
        num_list = list(map(int, input('리스트를 입력하세요 > ').split()))
        max = 0
        
        for num in num_list:
            if num > max:
                max = num
        print(max)
        ##########
        print()
       
    elif problem_number == '7':
        print('# 7. 양의 정수만 저장한 리스트가 주어집니다. 리스트에 저장된 정수 중 가장 작은 값을 출력하세요.\n\
단, min() 함수는 사용하지 마세요.')
        ########## solution code
        num_list = list(map(int, input('리스트를 입력하세요 > ').split()))
        min = num_list[0]
        
        for num in num_list:
            if num < min:
                min = num
        print(min)
        ##########
        print()
        
    else:
        print('Terminated!')
        break