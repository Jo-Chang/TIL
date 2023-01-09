f = open('./data/fruits.txt', 'r')
lines = f.readlines()
ans = 0
for line in lines:
    ans += 1
f.close()

with open('./02.txt', 'w') as f:
    f.write(str(ans))