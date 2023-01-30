import sys


def print_problem_info(str1, str2):
    print(f"\033[95m# {str1}. \x1b[96m{str2}\033[00m")


list_var = [0 for i in range(6)]
list_var = [1225, 2438, 2739, 2953, 2669]
dict_var = {
    list_var[0] : "이상한 곱셉",
    list_var[1] : "별 찍기 - 1",
    list_var[2] : "구구단",
    list_var[3] : "나는 요리사다",
    list_var[4] : "직사각형 네개의 합집합의 면적 구하기",
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
        def new_product(lst_):
            return sum([int(_) for _ in lst_[0]]) * sum([int(_) for _ in lst_[1]])

        print(new_product(sys.stdin.readline().split()))
        ####################
    
    
    elif problem_num == list_var[1]:
        print_problem_info(problem_num, dict_var[problem_num])
        
        #################### solution code
        def get_star_tree(n):
            return ["*" * m for m in range(1, n + 1)]


        print(*get_star_tree(int(sys.stdin.readline())), sep="\n")
        ####################
    
    
    elif problem_num == list_var[2]:
        print_problem_info(problem_num, dict_var[problem_num])
        
        #################### solution code
        def get_multiplication_table(n):
            return [f"{n} * {m} = {n * m}" for m in range(1, 10)]


        print(*get_multiplication_table(int(sys.stdin.readline())), sep="\n")
        ####################
    
    
    elif problem_num == list_var[3]:
        print_problem_info(problem_num, dict_var[problem_num])
        
        #################### solution code
        def get_winner(lst_):
            max_idx = 0
            max_sum = sum(lst_[max_idx])
            for idx in range(1, 5):
                temp_sum = sum(lst_[idx])
                if  temp_sum > max_sum:
                    max_sum = temp_sum
                    max_idx = idx
                    
            return max_idx + 1, max_sum


        # input
        score_lst = []
        for _ in range(5):
            score_lst.append(list(map(int, sys.stdin.readline().split())))

        # print
        print(*get_winner(score_lst))
        ####################
    
    
    elif problem_num == list_var[4]:
        print_problem_info(problem_num, dict_var[problem_num])
        
        #################### solution code
        MAX_POS = 100

        def sol_2d(lst_2d):
            ans = [[0] * MAX_POS for _ in range(MAX_POS)]
            for lst_ in lst_2d:
                for x in range(lst_[0], lst_[2]):
                    for y in range(lst_[1], lst_[3]):
                        ans[x][y] = 1
            
            # print("y\n")
            # for _ in range(9, -1, -1):
            #     print(f"{_} | ", end=" ")
            #     for __ in range(10):
            #         print(ans[__][_], end=" ")
            #     print()
            # print("  " + "-" * 22)
            # print(f"    ", *[m for m in range(10)], " x")
                
            return sum([sum(lst_) for lst_ in ans])

        def sol_set(lst_2d):
            ans = set()
            for lst_ in lst_2d:
                for x in range(lst_[0], lst_[2]):
                    for y in range(lst_[1], lst_[3]):
                        ans.add((x, y))
                        
            return len(ans)

        # input
        pos_lst2 = []
        for _ in range(4):
            pos_lst2.append(list(map(int, sys.stdin.readline().split())))

        # print
        # print(sol_2d(pos_lst2))
        print(sol_set(pos_lst2))
        ####################
        
        
    else:
        print("Terminated!")
        break


    print()