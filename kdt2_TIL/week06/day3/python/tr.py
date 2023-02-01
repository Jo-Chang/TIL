import sys


def print_problem_info(str1, str2):
    print(f"\033[95m# {str1}. \x1b[96m{str2}\033[00m")


list_var = [0 for i in range(6)]
list_var = [2525, 2798, 9076, 1526, 1436]
dict_var = {
    list_var[0] : "오븐 시계",
    list_var[1] : "블랙잭",
    list_var[2] : "점수 집계",
    list_var[3] : "가장 큰 금민수",
    list_var[4] : "영화 감독 숌",
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
        def get_time(h, m, t):
            ans_h = (h + (m + t) // 60) % 24
            ans_m = (m + t) % 60
            
            return ans_h, ans_m


        # input
        hour_num, minute_num = map(int, sys.stdin.readline().split())
        time_num = int(sys.stdin.readline())
        # print
        print(*get_time(hour_num, minute_num, time_num))
        ####################
    
    
    
    
    
    elif problem_num == list_var[1]:
        print_problem_info(problem_num, dict_var[problem_num])
        
        
        #################### solution code
        def get_closest_sum(n, lst_):
            len_ = len(lst_)
            lst_2 = []
            for i in range(len_ - 2):
                for j in range(i+1, len_ - 1):
                    for k in range(j+1, len_):
                        num_sum = lst_[i] + lst_[j] + lst_[k]
                        if num_sum <= n:
                            lst_2.append(num_sum)
                            # print(lst_[i], lst_[j], lst_[k], num_sum)
                            
            return max(lst_2)
            

        # input
        n_num, m_num = map(int, sys.stdin.readline().split())
        card_lst = list(map(int, sys.stdin.readline().split()))
        # print
        print(get_closest_sum(m_num, card_lst))
        ####################
    
    
    
    
    
    elif problem_num == list_var[2]:
        print_problem_info(problem_num, dict_var[problem_num])
        
        
        #################### solution code
        JUDGE_NUM = 5

        def is_KIN(lst_):
            sorted_lst = sorted(lst_)
            if sorted_lst[JUDGE_NUM - 2] - sorted_lst[1] > 3:
                return "KIN"
            else:
                return sum(sorted_lst) - sorted_lst[JUDGE_NUM - 1] - sorted_lst[0]
            
            # return "KIN" if sorted_lst[JUDGE_NUM - 2] - sroted_lst[1] > 3 else sum(sorted_lst) - sorted_lst[JUDGE_NUM - 1] -sorted_lst[0]

        # input
        for T in range(int(sys.stdin.readline())):
            score_lst = list(map(int, sys.stdin.readline().split()))
            # print
            print(is_KIN(score_lst))
        ####################
    
    
    
    
    
    elif problem_num == list_var[3]:
        print_problem_info(problem_num, dict_var[problem_num])
        
        
        #################### solution code
        def is_KEAUNMIN_num(num):
            temp_num = num
            while temp_num > 0:
                if temp_num % 10 != 4 and temp_num % 10 != 7:
                    return False
                temp_num //= 10
                
            return True
            
        def get_max_KEUNMIN_num(num):
            while not is_KEAUNMIN_num(num):
                num -= 1
                
            return num

        # input & print
        print(get_max_KEUNMIN_num(int(sys.stdin.readline())))
        ####################
    
    
    
    
    
    elif problem_num == list_var[4]:
        print_problem_info(problem_num, dict_var[problem_num])
        
        
        #################### solution code            
        def get_666_num(num):
            ans = 666
            cnt = 0
            while True:
                if "666" in str(ans):
                    cnt += 1
                    if cnt == num:
                        return ans
                ans += 1


        print(get_666_num(int(sys.stdin.readline())))
        ####################
        
        
        
        
        
    else:
        print("Terminated!")
        break


    print()