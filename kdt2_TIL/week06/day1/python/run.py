# run.py

import sys
PROBLEM_NUM = 1225
sys.stdin = open(f"{PROBLEM_NUM}.txt")

############
import sys


A, B = sys.stdin.readline().split()
total = 0
for i in A:
    for j in B:
        total += int(i) * int(j)

print(total)