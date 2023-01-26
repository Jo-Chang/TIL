# run.py for test

import sys
PROBLEM_NUM = 9012
# sys.stdin = open(f"{PROBLEM_NUM}.txt")

#####
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