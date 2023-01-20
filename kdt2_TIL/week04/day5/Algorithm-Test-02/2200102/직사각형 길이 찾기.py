# 3456. 직사각형 길이 찾기
import sys

sys.stdin = open("3456_직사각형_길이_찾기.txt")

##########

def last_length(len_lst):
    return_lst = []
    for len_num in len_lst:
        if len_num not in return_lst:
            return_lst.append(len_num)
        else:
            return_lst.remove(len_num)
            
    return return_lst[0]

for test_case in range(1, int(input()) + 1):
    answer = last_length(input().split())
    print(f"#{test_case} {answer}")