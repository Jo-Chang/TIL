# 1204. 최빈수 구하기
import sys

sys.stdin = open("1204_최빈수_구하기.txt")

##########

def get_frequent_score(scores):
    dict_var = {}
    for score in scores:
        dict_var[score] = dict_var.get(score, 0) + 1
    dict_var = sorted(dict_var.items(), key=lambda x: x[0], reverse=True)
    score_lst = sorted(dict_var, reverse=True, key=lambda x: x[1])
    
    return score_lst[0][0]

for T in range(1, int(input()) + 1):
    test_case = input()
    answer = get_frequent_score(list(map(int, input().split())))
    print(f"#{test_case} {answer}")