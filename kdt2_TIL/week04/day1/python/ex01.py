def print_problem_info(str1, str2):
    print(f"\033[95m# {str1}. \x1b[96m{str2}\033[00m")

dict_var = {
    "1000" : "A+B",
    "2558" : "A+B - 2",
    "10950" : "A+B - 3",
    "10953" : "A+B - 6",
    "11021" : "A+B - 7",
    "11022" : "A+B - 8",
}

while True:
    print("===아래 리스트에서 문제 번호 선택!===")
    for k, v in dict_var.items():
        print(f"\u001b[90m{k}. {v}\033[0m")

    problem_num = input("\n문제 번호 입력 > ")
    if problem_num == "1000":
        print_problem_info(problem_num, dict_var[problem_num])
        #################### solution code
        A, B = map(int, input().split())
        
        print(A + B)
        ####################
    
    elif problem_num == "2558":
        print_problem_info(problem_num, dict_var[problem_num])
        #################### solution code
        A = int(input())
        B = int(input())
        print(A + B)
        ####################
    
    elif problem_num == "10950":
        print_problem_info(problem_num, dict_var[problem_num])
        #################### solution code
        for T in range(1, int(input()) + 1):
            A, B = map(int, input().split())
            print(A+B)
        ####################
    
    elif problem_num == "10953":
        print_problem_info(problem_num, dict_var[problem_num])
        #################### solution code
        for T in range(1, int(input()) + 1):
            A, B = map(int, input().split(sep=","))
            print(A+B)
        ####################
    
    elif problem_num == "11021":
        print_problem_info(problem_num, dict_var[problem_num])
        #################### solution code
        for T in range(1, int(input()) + 1):
            A, B = map(int, input().split())
            print(f"Case #{T}: {A+B}")
        ####################
    
    elif problem_num == "11022":
        print_problem_info(problem_num, dict_var[problem_num])
        #################### solution code
        for T in range(1, int(input()) + 1):
            A, B = map(int, input().split())
            print(f"Case #{T}: {A} + {B} = {A+B}")
        ####################
        
    else:
        print("Terminated!")
        break

    print()