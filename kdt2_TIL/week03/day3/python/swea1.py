def print_problem_info(str_num, list):
    print(f"\033[95m# {str_num}. ", end= " ")
    for i in list:
        if i[0] == str_num:
            print(f"\x1b[96m{i[1]}\033[00m")

dict_var = {
    "2047" : "신문 헤드라인",
    "2025" : "N줄덧셈",
    "1936" : "1대1 가위바위보",
    "2027" : "대각선 출력하기",
    "2058" : "자릿수 더하기",
    "2019" : "더블더블",
}

dict_var = sorted(dict_var.items())

while True:
    
    print("===아래 리스트에서 문제 번호 선택!===")
    for k, v in dict_var:
        print(f"\u001b[90m{k}. {v}\033[0m")

    problem_num = input("\n문제 번호 입력 > ")
    print_problem_info(problem_num, dict_var)
    
    if problem_num == "2047":
        #################### solution code
        print(input().upper())
        ####################
    
    elif problem_num == "2025":
        #################### solution code
        n = int(input())
        print(n * (n + 1) // 2)
        ####################
        
    elif problem_num == "1936":
        #################### solution code
        A, B = map(int, input().split())

        B = B % 3 + 1
        if A == B:
            print("A")
        else:
            print("B")
        ####################
        
    elif problem_num == "2027":
        #################### solution code
        for i in range(5):
            print("+" * i, "#", "+" * (4 - i), sep = "")
        ####################
    
    elif problem_num == "2058":
        #################### solution code
        n = int(input())
        result = 0

        while n > 0:
            result += n % 10    
            n //= 10

        print(result)
        ####################
    
    elif problem_num == "2019":
        #################### solution code
        for i in range(int(input()) + 1):
            print(2**i, end = " ")
        ####################
        
    else:
        print("Terminated!")
        break

    print()