strings = []
strings.append('Hello, Python!')
for i in range(1, 6):
    strings.append(f'{i}일차 파이썬 공부중')

print(strings)

with open('01.txt.', 'w') as f:   
    for s in strings:
        f.write(s + '\n')