import sys


def print_problem_info(str1, str2):
    print(f"\033[95m# {str1}. \x1b[96m{str2}\033[00m")


list_var = [0 for i in range(6)]
list_var = [1547, 5576, 2846, 1251]
dict_var = {
    list_var[0] : "공",
    list_var[1] : "콘테스트",
    list_var[2] : "오르막길",
    list_var[3] : "단어 나누기",
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
        # input
        num_pair_lst = []
        for T in range(int(sys.stdin.readline())):
            x_num, y_num = map(int, sys.stdin.readline().split())
            num_pair_lst.append((x_num, y_num))

        # solution
        def find_ball(lst_):
            ball = 1
            for a, b in lst_:
                if a == ball:
                    ball = b
                elif b == ball:
                    ball = a

            if ball not in [1, 2, 3]:
                return -1

            return ball

        # print
        print(find_ball(num_pair_lst))
        # print(num_pair_lst)
        ####################
    
    
    
    
    
    elif problem_num == list_var[1]:
        print_problem_info(problem_num, dict_var[problem_num])
        
        
        #################### solution code
        # input
        w_participants_lst = []
        k_participants_lst = []

        for _ in range(10):
            score_num = int(sys.stdin.readline())
            # input error
            if not (0 <= score_num <= 100):
                print("Wrong Input!")
                
            w_participants_lst.append(score_num)
            
        for _ in range(10):
            score_num = int(sys.stdin.readline())
            # input error
            if not (0 <= score_num <= 100):
                print("Wrong Input!")
                
            k_participants_lst.append(score_num)


        # solution
        def high_3_sum(lst_):
            sorted_lst = sorted(lst_)
            
            return sum(sorted_lst[-3:])


        # print
        print(high_3_sum(w_participants_lst), high_3_sum(k_participants_lst))
        ####################
    
    
    
    
    
    elif problem_num == list_var[2]:
        print_problem_info(problem_num, dict_var[problem_num])
        
        
        #################### solution code
        #input
        sequence_num = int(sys.stdin.readline())
        sequence_lst = list(map(int, sys.stdin.readline().split()))


        # solution
        def get_increase_area(lst_):
            ans = 0
            len_ = len(lst_)
            
            cnt = 0
            for i in range(1, len_):
                if lst_[i - 1] < lst_[i]:
                    cnt += 1
                else:
                    distance = lst_[i - 1] - lst_[i - 1 - cnt]
                    ans = distance if distance > ans else ans
                    cnt = 0
            
            distance = lst_[len_ - 1] - lst_[len_ - 1 - cnt]
            ans = distance if distance > ans else ans
                        
            return ans


        # print
        print(get_increase_area(sequence_lst))
        ####################
    
    
    
    
    
    elif problem_num == list_var[3]:
        print_problem_info(problem_num, dict_var[problem_num])
        
        
        #################### solution code
        from itertools import combinations

        #input
        word = sys.stdin.readline().strip()
        if not word.islower():
            sys.exit("Input is not correct")


        # solution
        def get_split_reversed_word(word):
            lst_ = []
            split_lst = list(combinations(range(len(word) - 1), 2))
            
            for cut1, cut2 in split_lst:
                lst_.append(word[cut1::-1] + word[cut2:cut1:-1] + word[-1:cut2:-1])
            
            return min(lst_)


        # print
        print(get_split_reversed_word(word))
        ####################
    
    
    
    
       
    else:
        print("Terminated!")
        break


    print()