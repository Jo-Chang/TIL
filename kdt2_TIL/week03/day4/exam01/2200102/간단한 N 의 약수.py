# 1933. 간단한 N 의 약수

N = int(input())
list_div = []
for num in range(1, N // 2 + 1):
    if N % num == 0:
        list_div.append(num)
list_div.append(N)

print(*list_div)