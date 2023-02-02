# run.py

import sys
PROBLEM_NUM = 1251
sys.stdin = open(f"{PROBLEM_NUM}.txt")

#####

from itertools import combinations

#input
word = sys.stdin.readline().strip()
if not word.islower():
    sys.exit("Input is not correct")


# solution
def get_split_reversed_word(word):
    lst_ = []
    lst2_ = []
    split_lst = list(combinations(range(len(word) - 1), 2))
    for i in range(len(word)-2):
        for j in range(i + 1, len(word) - 1):
            for k in range(j + 1, len(word)):
                lst2_.append(word[:j][::-1] + word[j:k][::-1] + word[k:][::-1])
    
    # print(min(lst2_))
    # print(split_lst)
    
    for cut1, cut2 in split_lst:
        lst_.append(word[cut1::-1] + word[cut2:cut1:-1] + word[-1:cut2:-1])
    
    return min(lst_)


# print
print(get_split_reversed_word(word))