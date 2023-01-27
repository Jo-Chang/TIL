import heapq

numbers = [1, 100, 3, 5, 6, 20]

heapq.heapify(numbers)

print(numbers)

heapq.heappush(numbers, 0)
print(numbers)

heapq.heappop(numbers)
print(numbers)