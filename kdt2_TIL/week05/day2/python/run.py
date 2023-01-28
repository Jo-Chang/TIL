# run.py

import sys

PROBLEM_NUM = 11286
sys.stdin = open(f"{PROBLEM_NUM}.txt", encoding="UTF8")

#####
import heapq


num_lst = []

def sol(n):
    if n == 0:
        if num_lst:
            print(heapq.heappop(num_lst)[1])
        else:
            print(0)
    else:
        heapq.heappush(num_lst, (abs(n), n))


for T in range(int(sys.stdin.readline())):
    sol(int(sys.stdin.readline()))