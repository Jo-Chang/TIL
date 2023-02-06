# run.py

from pprint import pprint
import sys
PROBLEM_NUM = 4963
# sys.stdin = open(f"{PROBLEM_NUM}.txt")

#####

import sys


SEA = 0
LAND = 1
VISITED = 2


# solution
def find_land(lst2d_, stack):
    height = len(lst2d_)
    width = len(lst2d_[0])
    delta = [
        (-1, 0), (1, 0), (0, -1), (0, 1),
        (-1, -1), (-1, 1), (1, -1), (1, 1)
    ]
    
    while stack:
        x, y = stack.pop()
        for dx, dy in delta:
            x2 = x + dx
            y2 = y + dy
            if (x2 < 0) or (x2 >= height) or (y2 < 0) or (y2 >= width):
                # Finding out of area
                continue    # Skip
            
            if lst2d_[x2][y2] == LAND:
                stack.append((x2, y2))
                lst2d_[x2][y2] = VISITED  # Check visited land
                

def get_land_num(lst2d_):
    ans = 0
    height = len(lst2d_)
    width = len(lst2d_[0])
    
    for i in range(height):
        for j in range(width):
            stack = []
            if lst2d_[i][j] == LAND:   # Land not visited
                stack.append((i, j))
                lst2d_[i][j] = VISITED    # Check visited land
                find_land(lst2d_, stack)
                ans += 1
            
    return ans


# input & print
while True:
    width_num, height_num = map(int, sys.stdin.readline().split())
    if width_num == height_num == 0:    # End condition
        break
    
    # Input map shape
    map_shape_lst = []
    for _ in range(height_num):
        map_shape_lst.append(list(map(int, sys.stdin.readline().split())))
    
    print(*map_shape_lst, sep="\n")
    print(get_land_num(map_shape_lst))