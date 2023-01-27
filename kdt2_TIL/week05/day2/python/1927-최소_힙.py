# 1927. 최소 힙

import sys
import heapq

sys.stdin = open("1927.txt")


def min_heap(n, heap_):
    if n == 0:
        if heap_:
            print(heapq.heappop(heap_))
        else:
            print(0)
    else:
        heapq.heappush(heap_, n)
    
    
num_heap = []
for T in range(int(sys.stdin.readline())):
    min_heap(int(sys.stdin.readline()), num_heap)