# 1288. 새로운 불면증 치료법

for T in range(1, int(input()) + 1):
    list_num = [0 for i in range(10)]
    N = int(input())
    num = N
    
    while True:
        num2 = num
        while num2 > 0:
            list_num[num2 % 10] += 1
            num2 //= 10
        if not 0 in list_num:
            break
        num += N
        
    print(f"#{T} {num}")
    list_num.clear()