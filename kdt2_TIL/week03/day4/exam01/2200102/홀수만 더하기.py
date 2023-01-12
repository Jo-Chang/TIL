# 2072. 홀수만 더하기

for T in range(1, int(input()) + 1):
    num_list = map(int, input().split())
    sum = 0
    for n in num_list:
        if n % 2 == 1:
            sum += n
    print(f"#{T} {sum}")