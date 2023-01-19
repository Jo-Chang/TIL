import sys

sys.stdin = open("practice_dict_03.txt")

###########

members = input().split()
dict_var = {}

for member in members:
    dict_var[member] = dict_var.get(member, 0) + 1

min_foul = min(dict_var.values())

for key in dict_var.keys():
    if dict_var.get(key) == min_foul:
        print(key)
print(min_foul)