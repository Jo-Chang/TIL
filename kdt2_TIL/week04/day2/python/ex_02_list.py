def print_problem_info(str1, str2):
    print(f"\033[95m# {str1}. \x1b[96m{str2}\033[00m")

list_var = [0 for i in range(6)]
list_var = [10818, 11720, 2750, 2562]
dict_var = {
    list_var[0] : "최소, 최대",
    list_var[1] : "숫자의 합",
    list_var[2] : "수 정렬하기",
    list_var[3] : "최댓값",
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
        N = int(input())
        list_num = list(map(int, input().split()))

        print(min(list_num), max(list_num))
        ####################
    
    elif problem_num == list_var[1]:
        print_problem_info(problem_num, dict_var[problem_num])
        #################### solution code
        N = int(input())
        num_sum = 0
        for c in input():
            num_sum += int(c)

        print(num_sum)
        ####################
    
    elif problem_num == list_var[2]:
        print_problem_info(problem_num, dict_var[problem_num])
        #################### solution code
        N = int(input())

        list_num = []
        for i in range(N):
            list_num.append(int(input()))

        # list_num = sorted(list_num)
        list_num.sort()
        print(*list_num, sep="\n")
        ####################
    
    elif problem_num == list_var[3]:
        print_problem_info(problem_num, dict_var[problem_num])
        #################### solution code
        dict_var = {}

        for order in range(1, 10):
            num = int(input())
            dict_var[num] = order

        result = max(dict_var.items())
        print(result[0], result[1], sep ="\n")
        ####################
        
    else:
        print("Terminated!")
        break

    print()