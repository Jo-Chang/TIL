import sys
# sys.stdin = open("10773.txt")

num_lst = []
for idx in range(1, int(sys.stdin.readline()) + 1):
    num = int(sys.stdin.readline())
    if num == 0:
        num_lst.pop()
    else:
        num_lst.append(num)

print(sum(num_lst))