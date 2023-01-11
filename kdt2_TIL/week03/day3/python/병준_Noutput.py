import sys
sys.stdin = open("input (2).txt", "r")
a = sys.stdin.read()

print(a)
total = 0

for i in range(int(a)):
    total += i

print(total)