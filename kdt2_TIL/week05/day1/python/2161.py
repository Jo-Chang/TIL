# 2161. 카드 1

import sys

'''
# solution 1
num_lst = [num for num in range(1, int(sys.stdin.readline()) + 1)]

while len(num_lst) > 1:
    num = num_lst.pop(0)
    print(num)
    num = num_lst.pop(0)
    num_lst.append(num)
# 마지막 남은 카드 출력
print(*num_lst)
'''

# solution 2

from collections import deque

num_lst = deque(range(1, int(sys.stdin.readline()) + 1))

while len(num_lst) > 1:
    print(num_lst.popleft(), end=" ")
    num_lst.append(num_lst.popleft())
    
print(num_lst[0])