# run.py

import sys
PROBLEM_NUM = 1526
# sys.stdin = open(f"{PROBLEM_NUM}.txt")


#####
import sys

    
def get_666_num(num):
    ans = 666
    cnt = 0
    while True:
        if "666" in str(ans):
            cnt += 1
            if cnt == num:
                return ans
        ans += 1


print(get_666_num(int(sys.stdin.readline())))