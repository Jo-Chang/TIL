while True:
    num = int(input("정수를 입력하세요 > "))

    if num < 1:
        print("Wrong Input!")
        continue
    else:
        break
    
i = 1
sum = 0
while i <= num:
    sum += i
    i += 1

print(f"Total summ : {sum}")