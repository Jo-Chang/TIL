# run.py

import sys

PROBLEM_NUM = 11286
sys.stdin = open(f"{PROBLEM_NUM}.txt", encoding="UTF8")

#####
num_lst  = []

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
    
def my_heapify():
    idx = len(num_lst) - 1
    while idx > 0:
        parent = idx // 2
        if compare(num_lst[parent], num_lst[idx]):
            num_lst[parent], num_lst[idx] = num_lst[idx], num_lst[parent]
            idx = parent
        else:
            break
    
def my_pop():
    num_lst[0], num_lst[len(num_lst) - 1] = num_lst[len(num_lst) - 1], num_lst[0]
    idx = 0

    while 2*idx + 2 < len(num_lst) - 1:
        left = 2*idx + 1
        right = 2*idx + 2
        if abs(num_lst[left]) < abs(num_lst[right]): # left greater
            if compare(num_lst[idx], num_lst[right]):
                num_lst[idx], num_lst[left] = num_lst[left], num_lst[idx]
                idx = left
            else:
                break
        elif abs(num_lst[left]) == abs(num_lst[right]): # left-right even
            if num_lst[left] <= num_lst[right]:
                if compare(num_lst[idx], num_lst[left]):
                    num_lst[idx], num_lst[left] = num_lst[left], num_lst[idx]
                    idx = left
                else:
                    break
            else:
                if compare(num_lst[idx], num_lst[right]):
                    num_lst[idx], num_lst[right] = num_lst[right], num_lst[idx]
                    idx = right
                else:
                    break
        else: # right greater
            if compare(num_lst[idx], num_lst[right]):
                num_lst[idx], num_lst[right] = num_lst[right], num_lst[idx]
                idx = right
            else:
                break
    
    # after while - only left child
    last_left = 2*idx + 1
    if last_left == len(num_lst) - 2:
        if compare(num_lst[idx], num_lst[last_left]):
            num_lst[idx], num_lst[last_left] = num_lst[last_left], num_lst[idx]

    return num_lst.pop()
    
def sol(n):
    if n == 0:
        if num_lst:
            # print(f"pop : {num_lst}")
            print(my_pop())
            # print(f"after pop : {num_lst}")
        else:
            print(0)
    else:
        num_lst.append(n)
        # print(f"add : {num_lst}")
        my_heapify()
        # print(f"after heap: {num_lst}")


for T in range(int(sys.stdin.readline())):
    sol(int(sys.stdin.readline()))