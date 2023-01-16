def print_problem_info(str1, str2):
    print(f"\033[95m# {str1}. \x1b[96m{str2}\033[00m")

dict_var = {
    10039 : "평균 점수",
    10871 : "X보다 작은 수",
    2480 : "주사위 세개",
    10886 : "0 = not cute / 1 = cute",
    2506 : "점수계산",
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
    
    if problem_num == 10039:
        print_problem_info(problem_num, dict_var[problem_num])
        #################### solution code
        list_score = []
        for i in range(5):
            score = int(input())
            if score < 40:
                score = 40
            list_score.append(score)
            
        print(sum(list_score) // len(list_score))
        ####################
    
    elif problem_num == 10871:
        print_problem_info(problem_num, dict_var[problem_num])
        #################### solution code
        N, X = map(int, input().split())
        A = list(map(int, input().split()))
        
        for num in A:
            if num < X:
                print(num, end=" ")
        '''
        small_num = [n for n in t_nums if n < X]
        print(*small_nums)
        '''
        ####################
    
    elif problem_num == 2480:
        print_problem_info(problem_num, dict_var[problem_num])
        #################### solution code
        dict_num = [0 for i in range(6)]
        dice_roll = list(map(int, input().split()))
        for i in range(3):
            dict_num[dice_roll[i] - 1] += 1
            
        for i in range(1, 7):
            if dict_num[i - 1] == 3:
                price = 10000 + i * 1000
                break
            elif dict_num[i - 1] == 2:
                price = 1000 + i * 100
                break
            elif dict_num[i - 1] == 1:
                price = i * 100
            else:
                pass
        
        print(price)
        ####################
    
    elif problem_num == 10886:
        print_problem_info(problem_num, dict_var[problem_num])
        #################### solution code
        N = int(input())
        
        cute = 0
        for i in range(N):
            if int(input()) == 1:
                cute += 1
            
        if cute <= N // 2:
            print("Junhee is not cute!")
        else:
            print("Junhee is cute!")
        ####################
    
    elif problem_num == 2506:
        print_problem_info(problem_num, dict_var[problem_num])
        #################### solution code
        N = int(input())
        problem_score = list(map(int, input().split()))
        problem_result = []
        # problem_result = [0 for i in range(N)]
        
        accumulate = 0
        for i in range(N):
            if problem_score[i] == 1:
                accumulate += 1
                problem_result.append(accumulate)
            else:    # problem_score[i] == 0
                accumulate = 0
                problem_result.append(0)
                
        print(sum(problem_result))
        ####################
        
    else:
        print("Terminated!")
        break

    print()