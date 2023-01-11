import sys

def print_problem_number(number):
    print(f"\033[95m# {number}. \033[90m")

def set_print_default():
    print("\033[0m", end = "")
    
while True:
    
    problem_number = input("문제 번호 입력 > ")
    
    sys.stdin = open(f"tr1_0{problem_number}.txt", "r")
    if problem_number == "1":
        print_problem_number(problem_number)
        print("공백으로 구분된 정수")
        set_print_default()
        ########## solution code
        print(input())
        ##########
        
    elif problem_number == "2":
        print_problem_number(problem_number)
        print("공백으로 구분된 문자열")
        set_print_default()
        ########## solution code
        print(input())
        ##########
        
    elif problem_number == "3":
        print_problem_number(problem_number)
        print("테스트 케이스 수와 입력 줄 수가 주어지는 입력\n\
첫 줄에 테스트 케이스 수가 주어집니다.\n\
각 테스트 케이스의 첫 번째 줄에 입력 줄 수가 주어집니다.")
        set_print_default()
        ########## solution code
        T = int(input())
        for i in range(1, T + 1):
            L = int(input())
            for j in range(L):
                print(input())
        ##########
       
    elif problem_number == "4":
        print_problem_number(problem_number)
        print("테스트 케이스 수와 입력 줄 수가 주어지는 입력\n\
첫 줄에 테스트 케이스 수가 주어집니다.\n\
각 테스트 케이스의 첫 번째 줄에 입력 줄 수가 주어집니다.")
        set_print_default()
        ########## solution code
        T = int(input())
        for i in range(1, T + 1):
            L = int(input())
            print(L)
            for j in range(L):
                print(input())
        ##########
        
    elif problem_number == "5":
        print_problem_number(problem_number)
        print("테스트 케이스 수와 입력 줄 수가 주어지는 입력\n\
첫 줄에 테스트 케이스 수가 주어집니다.\n\
각 테스트 케이스의 첫 번째 줄에 입력 줄 수가 주어집니다.\n\
각 문장에 포함된 단어를 공백을 기준으로 출력하세요.")
        set_print_default()
        ########## solution code
        T = int(input())
        for i in range(1, T + 1):
            L = int(input())
            for j in range(L):
                print(input())
        ##########
        
    elif problem_number == "6":
        print_problem_number(problem_number)
        print("테스트 케이스 수와 입력 줄 수가 주어지는 입력\n\
첫 줄에 테스트 케이스 수가 주어집니다.\n\
각 테스트 케이스의 첫 번째 줄에 입력 줄 수가 주어집니다.")
        set_print_default()
        ########## solution code
        T = int(input())
        for i in range(1, T + 1):
            L = int(input())
            print(L)
            for j in range(L):
                print(input())
        ##########
       
    elif problem_number == "7":
        print_problem_number(problem_number)
        print("테스트 케이스 수와 입력 줄 수가 주어지는 입력\n\
첫 줄에 테스트 케이스와 각 테스트 케이스의 입력 줄 수가 주어집니다.")
        set_print_default()
        ########## solution code
        T, L = map(int, input().split())
        
        for i in range(L):
            print(input())
        ##########
        
    elif problem_number == "8":
        print_problem_number(problem_number)
        print("테스트 케이스 수와 입력 줄 수가 주어지는 입력\n\
첫 줄에 테스트 케이스와 각 테스트 케이스의 입력 줄 수가 주어집니다.")
        set_print_default()
        ########## solution code
        T, L = map(int, input().split())
        
        for i in range(L):
            print(input())
        ##########
       
    elif problem_number == "9":
        print_problem_number(problem_number)
        print("테스트 케이스 수와 입력 줄 수가 주어지는 입력\n\
첫 줄에 테스트 케이스와 각 테스트 케이스의 입력 줄 수가 주어집니다.")
        set_print_default()
        ########## solution code
        T, L = map(int, input().split())
        
        for i in range(L):
            print(input())
        ##########
        
    else:
        set_print_default()
        print("Terminated!")
        break
    
    print()