def print_problem_info(str1, str2):
    print(f"\033[95m# {str1}. \x1b[96m{str2}\033[00m")

list_var = [0 for i in range(6)]
list_var = [2576, 10822, 2754, 5622, 2577, 7785]
dict_var = {
    list_var[0] : "홀수",
    list_var[1] : "더하기",
    list_var[2] : "학점계산",
    list_var[3] : "다이얼",
    list_var[4] : "숫자의 개수",
    list_var[5] : "회사에 있는 사람",
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
        list_num = []
        for i in range(7):
            num = int(input())
            if num % 2 != 0:
                list_num.append(num)
            
        if len(list_num) == 0:
            print(-1)
        else:
            print(sum(list_num), min(list_num), sep="\n")
        ####################
    
    elif problem_num == list_var[1]:
        print_problem_info(problem_num, dict_var[problem_num])
        #################### solution code
        num_lst = list(map(int, input().split(sep=",")))
        print(sum(num_lst))
        ####################
    
    elif problem_num == list_var[2]:
        print_problem_info(problem_num, dict_var[problem_num])
        #################### solution code
        score_dict = {
            "A+": 4.3, "A0": 4.0, "A-": 3.7,
            "B+": 3.3, "B0": 3.0, "B-": 2.7,
            "C+": 2.3, "C0": 2.0, "C-": 1.7,
            "D+": 1.3, "D0": 1.0, "D-": 0.7,
            "F": 0.0,
        }

        # score1_dict = {
        #     "A": 4.0,
        #     "B": 3.0,
        #     "C": 2.0,
        #     "D": 1.0,
        #     "F": 0.0,
        # }
        # score2_dict = {
        #     "+": 0.3,
        #     "0": 0.0,
        #     "-": -0.3,
        # }

        print(score_dict.get(input()))
        ####################
    
    elif problem_num == list_var[3]:
        print_problem_info(problem_num, dict_var[problem_num])
        #################### solution code
        dial_dict = {
            "A": 2, "B": 2, "C": 2,
            "D": 3, "E": 3, "F": 3,
            "G": 4, "H": 4, "I": 4,
            "J": 5, "K": 5, "L": 5,
            "M": 6, "N": 6, "O": 6,
            "P": 7, "Q": 7, "R": 7, "S": 7,
            "T": 8, "U": 8, "V": 8,
            "W": 9, "X": 9, "Y": 9, "Z": 9,
            "OPERATOR": 0, 
        }
        # dial_dict = {
        #     "ABC": 2,
        #     "DEF": 3,
        #     "GHI": 4,
        #     "JKL": 5,
        #     "MNO": 6,
        #     "PQRS": 7,
        #     "TUV": 8,
        #     "WXYZ": 9,
        # }

        # 시간 맞추기
        TIME_GAP = 1
            
        words = input()
        time_sum = 0
        for word in words:
            time_sum += dial_dict[word] + TIME_GAP
        print(time_sum)
        ####################
    
    elif problem_num == list_var[4]:
        print_problem_info(problem_num, dict_var[problem_num])
        #################### solution code
        total_num = int(input()) * int(input()) * int(input())
        # str(total_num)
        num_dict = {}

        while total_num > 0:
            temp_num = total_num % 10
            num_dict[temp_num] = num_dict.get(temp_num, 0) + 1
            total_num //= 10

        for i in range(10):
            num_dict[i] = num_dict.get(i, 0)
        num_dict = dict(sorted(num_dict.items()))
        print(*num_dict.values(), sep="\n")
        ####################
    
    elif problem_num == list_var[5]:
        print_problem_info(problem_num, dict_var[problem_num])
        #################### solution code
        log_dict = {} 
        for i_num in range(int(input())):
            name, log = input().split()
            # name, log = sys.stdin.readline().split()
            # 훨씬 빠름!
            log_dict[name] = log

        left_name = [name for name in log_dict.keys() if log_dict[name] == "enter"]
        left_name.sort(reverse=True)

        print(*left_name, sep="\n")
        ####################
        
    else:
        print("Terminated!")
        break

    print()