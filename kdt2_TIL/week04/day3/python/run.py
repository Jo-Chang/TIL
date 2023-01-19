import sys

PROBLEM_NUM = 10988

sys.stdin = open(f"tr_01_{PROBLEM_NUM}.txt", encoding="UTF8")

#####

word = input()

i = 0
rev_i = len(word) - 1 - i
while i < len(word) - 1 - i:
    if word[i] != word[len(word) - 1 - i]:
        print(0)
        break
    i += 1
else:
    print(1)