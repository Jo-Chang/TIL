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
        N = int(input())

        count = 1
        temp_num = (N % 10) * 10 + (N // 10 + N % 10) % 10
        while temp_num != N:
            count += 1
            temp_num = (temp_num % 10) * 10 + (temp_num // 10 + temp_num % 10) % 10

        print(count)
        ####################
        
    else:
        print("Terminated!")
        break

    print()