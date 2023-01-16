def print_problem_info(str1, str2):
    print(f"\033[95m# {str1}. \x1b[96m{str2}\033[00m")

dict_var = {
    0 : "",
    1 : "",
    2 : "",
    3 : "",
    4 : "",
    5 : "",
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
    
    if problem_num == 0:
        print_problem_info(problem_num, dict_var[problem_num])
        #################### solution code
        pass
        ####################
    
    elif problem_num == 1:
        print_problem_info(problem_num, dict_var[problem_num])
        #################### solution code
        pass
        ####################
    
    elif problem_num == 2:
        print_problem_info(problem_num, dict_var[problem_num])
        #################### solution code
        pass
        ####################
    
    elif problem_num == 3:
        print_problem_info(problem_num, dict_var[problem_num])
        #################### solution code
        pass
        ####################
    
    elif problem_num == 4:
        print_problem_info(problem_num, dict_var[problem_num])
        #################### solution code
        pass
        ####################
    
    elif problem_num == 5:
        print_problem_info(problem_num, dict_var[problem_num])
        #################### solution code
        pass
        ####################
        
    else:
        print("Terminated!")
        break

    print()