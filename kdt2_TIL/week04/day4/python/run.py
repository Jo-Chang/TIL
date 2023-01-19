import sys

PROBLEM_NUM = 7785

sys.stdin = open(f"tr_01_{PROBLEM_NUM}.txt")

###########

log_dict = {} 
for i_num in range(int(input())):
    name, log = input().split()
    log_dict[name] = log

left_name = [name for name in log_dict.keys() if log_dict[name] == "enter"]
left_name.sort(reverse=True)

print(*left_name, sep="\n")