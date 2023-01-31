import sys
PROBLEM_NUM = 1652
# sys.stdin = open(f"{PROBLEM_NUM}.txt")

#####

import sys


#2592 대표값
#mport sys
# sys.stdin = open("input.txt")

N_list = []
for i in range(10):
    N = int(input())
    N_list.append(N)

# print(N_list)
print(int(sum(N_list)/10))

temp = {}
for j in N_list:
    if j in temp:
        temp[j] += 1
    else:
        temp[j] = 1
max_li = temp.values()
most = 0
for x in temp:
    print(f"x : {x}")
    if temp[x] == max(max_li):
        most = x
#print(temp)
#print(max_li)
print(most)