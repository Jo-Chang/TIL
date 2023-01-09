result = ['1', '5', '3', '4']

text = ''
for elem in result:
    text = text + elem
print(text)

# (2-2) join 메서드
print(''.join(result))

# 1 5 3 4
print(' '.join(result))