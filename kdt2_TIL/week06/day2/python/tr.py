import sys


def print_problem_info(str1, str2):
    print(f"\033[95m# {str1}. \x1b[96m{str2}\033[00m")


list_var = [0 for i in range(6)]
list_var = [2441, 2592, 10798, 9455, 1652]
dict_var = {
    list_var[0] : "별 찍기 - 4",
    list_var[1] : "대표값",
    list_var[2] : "세로 읽기",
    list_var[3] : "박스",
    list_var[4] : "누울 자리를 찾아라",
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
        def print_star(num):
            for i in range(num):
                print(" " * i + "*" * (num-i))
                
            
        print_star(int(sys.stdin.readline()))
        ####################
    
    
    
    
    
    elif problem_num == list_var[1]:
        print_problem_info(problem_num, dict_var[problem_num])
        
        
        #################### solution code
        def representational_num(dict_):
            max_tuple = max(dict_.items(), key=lambda x: x[1])
            mean_ = 0
            for mem in dict_.items():
                mean_ += mem[0] * mem[1]
            mean_ //= sum(dict_.values())
            
            return (mean_, max_tuple[0])


        num_dict = {}
        for _ in range(10):
            num = int(sys.stdin.readline())
            num_dict[num] = num_dict.get(num, 0) + 1
            
        print(*representational_num(num_dict), sep="\n")
        ####################
    
    
    
    
    
    elif problem_num == list_var[2]:
        print_problem_info(problem_num, dict_var[problem_num])
        
        
        #################### solution code
        WORDS_NUM = 5

        def print_transpose(lst2_):
            ans = ""
            
            for i in range(max([len(word) for word in lst2_])):
                for j in range(WORDS_NUM):
                    if i < len(lst2_[j]):
                        ans += lst2_[j][i]
                        
            print(ans)


        # input
        word_lst2 = []
        for _ in range(WORDS_NUM):
            word_lst2.append(sys.stdin.readline().strip())
            
        print_transpose(word_lst2)
        ####################
    
    
    
    
    
    elif problem_num == list_var[3]:
        print_problem_info(problem_num, dict_var[problem_num])
        
        
        #################### solution code
        def get_move_box_num(lst2_):
            ans = 0
            y_len = len(lst2_)
            x_len = len(lst2_[0])
            for i in range(x_len):
                cnt = 0
                for j in range(y_len-1, -1, -1):
                    if lst2_[j][i] == 1:
                        ans += (y_len - 1 - cnt) - j
                        cnt += 1
                
            return ans
            

        # input
        for T in range(int(sys.stdin.readline())):
            n_num, m_num = map(int, sys.stdin.readline().split())
            map_lst2 = []
            for _ in range(n_num):
                map_lst2.append(list(map(int, sys.stdin.readline().split())))
            print(get_move_box_num(map_lst2))
        ####################
    
    
    
    
    
    elif problem_num == list_var[4]:
        print_problem_info(problem_num, dict_var[problem_num])
        
        
        #################### solution code
        def get_positions_num(lst_):
            ans_row, ans_col = 0, 0
            len_ = len(lst_)
            
            for i in range(len_):
                accumulate1 = 0
                accumulate2 = 0
                for j in range(len_):
                    # width count
                    if lst_[i][j] == "X":
                        if accumulate1 > 1:
                            ans_row += 1
                        accumulate1 = 0
                    else:
                        accumulate1 += 1
                        
                    # height count
                    if lst_[j][i] == "X":
                        if accumulate2 > 1:
                            ans_col += 1
                        accumulate2 = 0
                    else:
                        accumulate2 += 1
                        
                if accumulate1 > 1:
                    ans_row += 1
                if accumulate2 > 1:
                    ans_col += 1
            
            return ans_row, ans_col


        # input
        position_lst = []
        for T in range(int(sys.stdin.readline())):
            position_lst.append(sys.stdin.readline().strip())
        # position_lst = [int(sys.stdin.readline.strip()) for _ in range(WORDS_NUM)]
            
        print(*get_positions_num(position_lst))
        ####################
        
        
        
        
        
    else:
        print("Terminated!")
        break


    print()