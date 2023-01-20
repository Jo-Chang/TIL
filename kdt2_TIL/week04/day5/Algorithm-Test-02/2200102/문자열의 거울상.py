# 10804. 문자열의 거울상
import sys

sys.stdin = open("10804_문자열의_거울상.txt")

##########

def invert_string(word):
    string = "bdpq"
    reversed = "dbqp"
    reversed_word = ""
    for word_i in range(len(word)):
        index = string.find(word[word_i])
        # print(f"index : {index}")
        reversed_word += reversed[index]
    
    return reversed_word[::-1]

for test_case in range(1, int(input()) + 1):
    reversed_word = invert_string(input())
    print(f"#{test_case} {reversed_word}")