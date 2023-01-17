numbers = [10, 2, 5, 7]

for number in numbers:
    if number & 2 ==0:
        numbers.pop()
    print(number)
    
print("=====")
numbers = [10, 2, 5, 7]
for i in range(len(numbers)):
    print(i)