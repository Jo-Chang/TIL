first = list(map(int,input().split()))
second = list(map(int,input().split()))
third = list(map(int,input().split()))
lst = [first, second, third]

# 하나의 리스트'l_lst'에 정수형태로 모두 넣는다.
l_lst = []
for loc in lst:
    # for l in loc:
    l_lst.append(loc)
print(l_lst)

# 'l_lst'를 돌려보며 해당 숫자의 개수가 홀수고 새로운 리스트에 없다면 추가한다.
new_lst = []
for number in l_lst:
    print(f"number : {number}")
    if l_lst.count(number[0])%2 != 0:
        if number[0] not in new_lst:
            new_lst.append(number)
        elif l_lst.count(number[0])%2 == 0:
            print(l_lst.count(number))
            print(number)
            new_lst.append(number)
            
    if l_lst.count(number[1])%2 != 0:
        if number[1] not in new_lst:
            new_lst.append(number[1])
        elif l_lst.count(number[1])%2 == 0:
            print(l_lst.count(number))
            print(number)
            new_lst.append(number)

print(*new_lst)