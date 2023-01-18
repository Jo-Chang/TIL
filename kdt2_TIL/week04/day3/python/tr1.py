def print_problem_info(str1, str2):
    print(f"\033[95m# {str1}. \x1b[96m{str2}\033[00m")

list_var = [0 for i in range(6)]
list_var = [9498, 9093, 11721, 2947]
dict_var = {
    list_var[0] : "시험 성적",
    list_var[1] : "단어 뒤집기",
    list_var[2] : "열 개씩 끊어 출력하기",
    list_var[3] : "나무 조각",
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
        score_num = int(input())

        if score_num >= 90:
            print("A")
        elif score_num >= 80:
            print("B")
        elif score_num >= 70:
            print("C")
        elif score_num >= 60:
            print("D")
        else:
            print("F")
        ####################
    
    elif problem_num == list_var[1]:
        print_problem_info(problem_num, dict_var[problem_num])
        #################### solution code
        for test_case in range(1, int(input()) + 1):
            words = input().split()
            for word in words:
                print(word[::-1], end= " ")
            print()
        ####################
    
    elif problem_num == list_var[2]:
        print_problem_info(problem_num, dict_var[problem_num])
        #################### solution code
        sentence = input()

        for i_num in range(1, len(sentence) // 10 + 1):
            print(sentence[10*(i_num - 1):10*i_num])
        print(sentence[len(sentence) // 10 * 10:])
        ####################
    
    elif problem_num == list_var[3]:
        print_problem_info(problem_num, dict_var[problem_num])
        #################### solution code
        num_order = list(map(int, input().split()))

        while num_order != [1, 2, 3, 4, 5]:
            for i in range(len(num_order) - 1):
                if num_order[i] > num_order[i+1]:
                    num_order[i], num_order[i+1] = num_order[i+1], num_order[i]
                    print(*num_order)
        ####################
        
    else:
        print("Terminated!")
        break

    print()