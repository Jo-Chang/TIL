import sys


def print_problem_info(str1, str2):
    print(f"\033[95m# {str1}. \x1b[96m{str2}\033[00m")


list_var = [0 for i in range(6)]
list_var = [10101, 2720, 1453, 10773, 2161, 9012]
dict_var = {
    list_var[0] : "삼각형 외우기",
    list_var[1] : "세탁소 사장 동혁",
    list_var[2] : "피시방 알바",
    list_var[3] : "제로",
    list_var[4] : "카드 1",
    list_var[5] : "괄호",
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
        def get_triangle(lst_):
            if sum(lst_) != 180:
                return "Error"
            else:
                for mem in lst_:
                    if lst_.count(mem) == 3:
                        return "Equilateral"
                    elif lst_.count(mem) == 2:
                        return "Isosceles"
                return "Scalene"
            
            
        degree_lst = []
        for i in range(3):
            degree_lst.append(int(sys.stdin.readline()))
            
        print(get_triangle(degree_lst))
        ####################
    
    
    elif problem_num == list_var[1]:
        print_problem_info(problem_num, dict_var[problem_num])
        
        #################### solution code
        def get_changes(num):
            lst = []
            num_lst = [25, 10, 5, 1]
            
            for i in num_lst:
                lst.append(num // i)
                num %= i
            # lst.append(num // 25)
            # num %= 25
            # lst.append(num // 10)
            # num %= 10
            # lst.append(num // 5)
            # num %= 5
            # lst.append(num)
            
            return lst


        for T in range(int(sys.stdin.readline())):
            print(*get_changes(int(sys.stdin.readline())))
        ####################
    
    
    elif problem_num == list_var[2]:
        print_problem_info(problem_num, dict_var[problem_num])
        
        #################### solution code
        def get_rejected(lst_):
            cnt = 0
            
            lst_2 = []
            for i in lst_:
                if i in lst_2:
                    cnt += 1
                else:
                    lst_2.append(i)
            
            return cnt


        people_num = int(sys.stdin.readline())
        num_lst = list(map(int, sys.stdin.readline().split()))
        print(get_rejected(num_lst))
        ####################
    
    
    elif problem_num == list_var[3]:
        print_problem_info(problem_num, dict_var[problem_num])
        
        #################### solution code
        num_lst = []
        for idx in range(1, int(sys.stdin.readline()) + 1):
            num = int(sys.stdin.readline())
            if num == 0:
                num_lst.pop()
            else:
                num_lst.append(num)

        print(sum(num_lst))
        ####################
    
    
    elif problem_num == list_var[4]:
        print_problem_info(problem_num, dict_var[problem_num])
        
        #################### solution code
        from collections import deque


        def get_card_order(num):
            ans = []
            lst_ = deque(range(1, num + 1))

            while len(lst_) > 1:
                ans.append(lst_.popleft())
                lst_.append(lst_.popleft())
            ans.append(lst_.pop())
            
            return ans


        print(*get_card_order(int(sys.stdin.readline())))
        ####################
    
    
    elif problem_num == list_var[5]:
        print_problem_info(problem_num, dict_var[problem_num])
        
        #################### solution code
        def is_correct_VPS(sentence):
            stack = []
            for ch in sentence:
                if ch == ")":
                    try:
                        stack.pop()
                    except:
                        return "NO"
                else:
                    stack.append(ch)
            
            if len(stack) == 0:
                return "YES"
            else:
                return "NO"


        for T in range(1, int(sys.stdin.readline()) + 1):
            # print(f"#{T} : ")
            print(is_correct_VPS(sys.stdin.readline().strip()))
        ####################
        
        
    else:
        print("Terminated!")
        break

    print()