import sys


def print_problem_info(str1, str2):
    print(f"\033[95m# {str1}. \x1b[96m{str2}\033[00m")


list_var = [0 for i in range(6)]
list_var = [10817, 20001, 1269, 3052, 1181, 11286]
dict_var = {
    list_var[0] : "세 수",
    list_var[1] : "고무오리 디버깅",
    list_var[2] : "대칭 차집합",
    list_var[3] : "나머지",
    list_var[4] : "단어 정렬",
    list_var[5] : "절댓값 힙",
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
        import heapq


        def get_second_max(lst_):
            heapq.heapify(lst_)
            heapq.heappop(lst_)
            return heapq.heappop(lst_)


        print(get_second_max(list(map(int, sys.stdin.readline().split()))))
        ####################
    
    
    elif problem_num == list_var[1]:
        print_problem_info(problem_num, dict_var[problem_num])
        
        #################### solution code
        cmd_lst = ["고무오리 디버깅 시작", "문제", "고무오리", "고무오리 디버깅 끝"]

        def debugging_end(lst_):
            if lst_:
                print("힝구")
            else:
                print("고무오리야 사랑해")


        if sys.stdin.readline().strip() != cmd_lst[0]:
            print("Wrong Input!")
        else:
            input_cmd_lst = []
            while True:
                command = sys.stdin.readline().strip()
                if command == cmd_lst[3]:
                    debugging_end(input_cmd_lst)
                    break
                elif command == cmd_lst[1]:
                    input_cmd_lst.append(command)
                elif command == cmd_lst[2]:
                    if input_cmd_lst:
                        input_cmd_lst.pop()
                    else:
                        input_cmd_lst.append(cmd_lst[1])
                        input_cmd_lst.append(cmd_lst[1])
        ####################
    
    
    elif problem_num == list_var[2]:
        print_problem_info(problem_num, dict_var[problem_num])
        
        #################### solution code
        def get_symmetric_diff_num(a, b):
            return len([ele for ele in a if ele not in b] + [ele for ele in b if ele not in a])


        a_num, b_num = map(int, sys.stdin.readline().split())

        a_set = set(list(map(int, sys.stdin.readline().split())))
        b_set = set(list(map(int, sys.stdin.readline().split())))

        print(get_symmetric_diff_num(a_set, b_set))
        ####################
    
    
    elif problem_num == list_var[3]:
        print_problem_info(problem_num, dict_var[problem_num])
        
        #################### solution code
        def get_mod42_set(lst_):
            return set([mem%42 for mem in lst_])


        nums = []
        for T in range(10):
            nums.append(int(sys.stdin.readline()))
            
        print(len(get_mod42_set(nums)))
        ####################
    
    
    elif problem_num == list_var[4]:
        print_problem_info(problem_num, dict_var[problem_num])
        
        #################### solution code
        def my_sort(x):
            return len(x), x
            
        def get_my_dict(lst_):
            return sorted(lst_, key=my_sort)


        word_lst = set([])
        for T in range(int(sys.stdin.readline())):
            word_lst.add(sys.stdin.readline().strip())
            
        print(*get_my_dict(word_lst), sep="\n")
        ####################
    
    
    elif problem_num == list_var[5]:
        print_problem_info(problem_num, dict_var[problem_num])
        
        #################### solution code
        pass
        ####################
        
        
    else:
        print("Terminated!")
        break


    print()