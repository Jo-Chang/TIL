# 14649. 신용카드 만들기 1
import sys

sys.stdin = open("14649_신용카드_만들기_1.txt")

##########

def LUHN_number(num_lst):
    num_sum = 0
    for i in range(1, len(num_lst) + 1):
        if i % 2 == 0:
            num_sum += num_lst[i - 1]
        else:
            num_sum += num_lst[i - 1] * 2
    
    return (10 - num_sum) % 10
    
for test_case in range(1, int(input())+1):
    num_16th = LUHN_number(list(map(int, input().split())))
    print(f"#{test_case} {num_16th}")