# run.py

import sys

PROBLEM_NUM = 11286
sys.stdin = open(f"{PROBLEM_NUM}.txt", encoding="UTF8")

#####
from collections import deque

num_deq = deque([])

def my_heapify():
    idx = len(num_deq) - 1
    while idx > 0:
        if abs(num_deq[idx]) < abs(num_deq[idx//2]):
            num_deq[idx], num_deq[idx//2] = num_deq[idx//2], num_deq[idx]
        elif abs(num_deq[idx]) == abs(num_deq[idx//2]):
            if num_deq[idx] < num_deq[idx//2]:
                num_deq[idx], num_deq[idx//2] = num_deq[idx//2], num_deq[idx]
            else:
                break
        else:
            break
        idx //= 2

def my_pop():
    num_deq[0], num_deq[len(num_deq) - 1] = num_deq[len(num_deq) - 1], num_deq[0]
    
    idx = 0
    while 2*idx + 2 < len(num_deq) - 1:
        if abs(num_deq[idx]) < abs(num_deq[2*idx + 1]) or abs(num_deq[idx]) < abs(num_deq[2*idx + 2]):
            if abs(num_deq[2*idx + 1]) < abs(num_deq[2*idx + 2]): # left greater
                num_deq[idx], num_deq[2*idx + 1] = num_deq[2*idx + 1], num_deq[idx]
                idx = 2*idx + 1
            elif abs(num_deq[2*idx + 1]) == abs(num_deq[2*idx + 2]): # left-right even
                if num_deq[2*idx + 1] < num_deq[2*idx + 2]:
                    num_deq[idx], num_deq[2*idx + 1] = num_deq[2*idx + 1], num_deq[idx]
                    idx = 2*idx + 1
                else:
                    num_deq[idx], num_deq[2*idx + 2] = num_deq[2*idx + 2], num_deq[idx]
                    idx = 2*idx + 2
            else: # right greater
                num_deq[idx], num_deq[2*idx + 2] = num_deq[2*idx + 2], num_deq[idx]
                idx = 2*idx + 2
        else:
            break
    
    return num_deq.pop()
    
def sol(n):
    if n == 0:
        if num_deq:
            print(my_pop())
        else:
            print(0)
    else:
        num_deq.append(n)
        my_heapify()


for T in range(int(sys.stdin.readline())):
    sol(int(sys.stdin.readline()))