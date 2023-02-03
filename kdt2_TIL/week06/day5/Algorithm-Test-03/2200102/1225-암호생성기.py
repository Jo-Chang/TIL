# 1225. 암호생성기


from collections import deque


# solution
def get_password_num(lst_):
    LEN = len(lst_)
    
    cnt = 1
    while True:
        num = lst_.popleft()
        num = num - cnt if num > cnt else 0
        lst_.append(num)
        
        if num == 0:
            return lst_
        
        cnt = cnt + 1 if cnt < 5 else 1
        
    
# input, print
TEST_CASE = 10

for T in range(TEST_CASE ):
    test_case = int(input())
    num_lst = deque(map(int, input().split()))
    
    print(f"#{test_case}", *get_password_num(num_lst))