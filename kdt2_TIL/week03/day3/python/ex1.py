while True:
    example_number = input("문제 번호 입력 (문제 번호 외 입력시 종료)> ")
    print(f"\033[95m# {example_number}\033[0m")
    if example_number == "1":
        print("# 정수 1개 입력 받기")
        ########## training code
        number = int(input())

        print(number)
        ##########
        
    elif example_number == "2":
        print("# 공백으로 구분된 여러개의 정수 입력 받기")
        ########## training code
        numbers = list(map(int,input().split()))

        print(numbers)
        ##########
        
    elif example_number == "3":
        print("# 공백으로 구분된 여러개의 단어 입력 받기")
        ########## training code 
        string = input().split()

        print(string)
        ##########
        
    elif example_number == "4":
        print("# 공백으로 구분된 2개의 정수 입력 받기")
        ########## training code
        a, b = list(map(int,input().split()))

        print(a, b)
        ##########
        
    elif example_number == "5":
        print("# 테스트 케이스 수가 주어지는 입력 받기")
        ########## training code
        T = int(input()) # 테스트 케이스 수

        for t in range(1, T+1):
            print(t)
            # 이하 입력 코드
            pass
        ##########
        
    elif example_number == "6":
        print("# 입력 줄 수가 주어지는 입력 받기")
        ########## training code
        N = int(input()) # 입력 줄 수

        for _ in range(N):
            # 이하 입력 코드
            pass
        ##########
        
    elif example_number == "7":
        print("# 테스트 케이스와 입력 줄 수가 주어지는 입력 받기")
        ########## training code
        T = int(input()) # 테스트 케이스 수

        for t in range(1, T + 1):
            N = int(input()) # 입력 줄 수
            
            for _ in range(N):
                # 이하 입력 코드
                pass
        ##########
        
    elif example_number == "8":
        print("# 파일 입력\n\
# input.txt 파일을 생성하고,입력을 작성해주세요.\n\
# 코드를 알고리즘 사이트에 제출할 때 아래 두 줄은 주석처리 해주세요.")
        ########## training code
        import sys
        sys.stdin = open("input.txt", "r")

        # 이하 입력 코드
        ##########

    else:
        print("Terminated!")
        break
    
    print()










 
