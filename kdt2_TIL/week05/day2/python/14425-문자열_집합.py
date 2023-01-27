# 14425. 문자열 집합

import sys

sys.stdin = open("14425.txt")


def is_set(set_, word):
    return word in set_


set_size, word_num = map(int, sys.stdin.readline().split())

# set 생성
word_lst = []
for T in range(set_size):
    word_lst.append(sys.stdin.readline())
word_set = set(word_lst)

# set 판별
cnt = 0
for T in range(word_num):
    cnt += is_set(word_set, sys.stdin.readline())
        
print (cnt)