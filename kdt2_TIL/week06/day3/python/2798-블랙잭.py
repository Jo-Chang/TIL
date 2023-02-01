# run.py

import sys
PROBLEM_NUM = 2798
sys.stdin = open(f"{PROBLEM_NUM}.txt")


#####

import sys


def get_closest_sum(n, lst_):
    len_ = len(lst_)
    lst_2 = []
    for i in range(len_ - 2):
        for j in range(i+1, len_ - 1):
            for k in range(j+1, len_):
                num_sum = lst_[i] + lst_[j] + lst_[k]
                if num_sum <= n:
                    lst_2.append(num_sum)
                    # print(lst_[i], lst_[j], lst_[k], num_sum)
                    
    return max(lst_2)
    

n_num, m_num = map(int, sys.stdin.readline().split())
card_lst = list(map(int, sys.stdin.readline().split()))

print(get_closest_sum(m_num, card_lst))