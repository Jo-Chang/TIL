# run.py

import sys
PROBLEM_NUM = 1526
# sys.stdin = open(f"{PROBLEM_NUM}.txt")


#####
import sys
from itertools import chain

    
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(*list(chain(*matrix)))