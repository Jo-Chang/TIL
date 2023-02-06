# 11286. 절댓값 힙

import sys

PROBLEM_NUM = 11286
sys.stdin = open(f"{PROBLEM_NUM}.txt", encoding="UTF8")

#####

import sys


def compare(a, b):
    if abs(a) > abs(b):
        return True
    elif abs(a) == abs(b):
        if a > b:
            return True
        else:
            return False
    else:
        return False
    
def my_heappush(num_lst, n):
    num_lst.append(n)
    
    idx = len(num_lst) - 1
    # Upheap
    while idx > 0:
        parent = (idx - 1) // 2
        if compare(num_lst[parent], num_lst[idx]):
            num_lst[parent], num_lst[idx] = num_lst[idx], num_lst[parent]
            idx = parent
        else:
            break
    
def my_heappop(num_lst):
    num_lst[0], num_lst[len(num_lst) - 1] = num_lst[len(num_lst) - 1], num_lst[0]
    idx = 0

    # DownHeap
    while 2*idx + 2 < len(num_lst) - 1:
        left = 2*idx + 1
        right = 2*idx + 2
        if compare(num_lst[left], num_lst[right]): # Case - left greater 
            if compare(num_lst[idx], num_lst[right]):
                num_lst[idx], num_lst[right] = num_lst[right], num_lst[idx]
                idx = right
            else:
                break
        else: # Case - right greater
            if compare(num_lst[idx], num_lst[left]):
                num_lst[idx], num_lst[left] = num_lst[left], num_lst[idx]
                idx = left
            else:
                break
    
    # Case - after while (only left child)
    last_left = 2*idx + 1
    if last_left == len(num_lst) - 2:
        if compare(num_lst[idx], num_lst[last_left]):
            num_lst[idx], num_lst[last_left] = num_lst[last_left], num_lst[idx]

    # Remove and return ex-root node
    return num_lst.pop()
    
def sol(num_lst, n):
    if n == 0:
        if num_lst:
            # print(f"pop : {num_lst}")
            print(my_heappop(num_lst))
            # print(f"after pop : {num_lst}")
        else:
            print(0)
    else:
        # print(f"add : {num_lst}")
        my_heappush(num_lst, n)
        # print(f"after heap: {num_lst}")


num_lst  = []
for T in range(int(sys.stdin.readline())):
    sol(num_lst, int(sys.stdin.readline()))