# 7568 input_example generator

import sys
import random

PROBLEM_NUM = 7568

with open(f"{PROBLEM_NUM}.txt", "w") as f:
    people_num = random.randrange(2, 51)
    f.write(str(people_num)+"\n")
    
    for _ in range(people_num):
        weight = random.randrange(10, 201)
        height = random.randrange(10, 201)
        f.write(f"{str(weight)} {str(height)}\n")