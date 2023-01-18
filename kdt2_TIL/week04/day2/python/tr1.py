def print_problem_info(str1, str2):
    print(f"\033[95m# {str1}. \x1b[96m{str2}\033[00m")

list_var = [0 for i in range(6)]
list_var = [9085, 10824, 3009, 10952, 1110]
dict_var = {
    list_var[0] : "더하기",
    list_var[1] : "네 수",
    list_var[2] : "네 번째 점",
    list_var[3] : "A+B - 5",
    list_var[4] : "더하기 사이클",
}

dict_var = dict(sorted(dict_var.items()))

while True:
    print("===아래 리스트에서 문제 번호 선택!===")
    for k, v in dict_var.items():
        print(f"\u001b[90m{k}. {v}\033[0m")

    try:
        problem_num = int(input("\n문제 번호 입력 > "))
    except:
        print("Terminated!")
        break
    
    if problem_num == list_var[0]:
        print_problem_info(problem_num, dict_var[problem_num])
        #################### solution code
        for T in range(1, int(input()) + 1):
            N = int(input())
            list_num = list(map(int, input().split()))
            print(sum(list_num))
        ####################
    
    elif problem_num == list_var[1]:
        print_problem_info(problem_num, dict_var[problem_num])
        #################### solution code
        A, B, C, D = input().split()
        print(int(A + B) + int(C + D))
        ####################
    
    elif problem_num == list_var[2]:
        print_problem_info(problem_num, dict_var[problem_num])
        #################### solution code
        list_x = []
        list_y = []
        for i in range(3):
            x, y = map(int, input().split())
            
            if x in list_x:
                list_x.remove(x)
            else:
                list_x.append(x)
                
            if y in list_y:
                list_y.remove(y)
            else:
                list_y.append(y)
                
        print(*list_x, *list_y)
        ####################
    
    elif problem_num == list_var[3]:
        print_problem_info(problem_num, dict_var[problem_num])
        #################### solution code
        while True:
            A, B = map(int, input().split())
            if A == 0 and B == 0:
                break
            print(A+B)
        ####################
    
    elif problem_num == list_var[4]:
        print_problem_info(problem_num, dict_var[problem_num])
        #################### solution code
        '''
        N = int(input())

        count = 1
        temp_num = (N % 10) * 10 + (N // 10 + N % 10) % 10
        while temp_num != N:
            count += 1
            temp_num = (temp_num % 10) * 10 + (temp_num // 10 + temp_num % 10) % 10

        print(count)
        '''
        # Sol by string
        N = input()
        
        # 먼저 주어진 수가 10보다 작다면 앞에 0을 붙여 두 자리 수로 만든다.
        if int(N) < 10:
            N = "0" + N
                
        # N을 복사한 변수
        given_n = N
                
        # 사이클 횟수
        cnt = 0
        while True:
            
            # 각 자리의 숫자를 더한다.
            first = N[-1]
            second = N[0]
            
            sum_number = int(first) + int(second)
            
            # 주어진 수의 가장 오른쪽 자리 수와 앞에서 구한 합의 가장 오른쪽 자리 수를 이어 붙이면 새로운 수를 만들 수 있다.
            # 주어진 수 N
            # 구한 합 sum_number
            
            new_number = N[-1] + str(sum_number)[-1]
            
            print(new_number)
            
            # 연산 횟수 증가(사이클 횟수 증가)
            cnt += 1
            
            if new_number == given_n:
                break
            
            # new_number를 다시 N에 넣어줘요.
            # N의 값을 새로운 수를 저장하면?
            N = new_number
            
        print(cnt)
        
        ####################
        
    else:
        print("Terminated!")
        break

    print()