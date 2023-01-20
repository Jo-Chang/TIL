# 14654. 신용카드 만들기 2
import sys

sys.stdin = open("14654_신용카드_만들기_2.txt")

##########

def is_card(card_str):
    if card_str[0] not in "34569":
        return 0
    card_str = card_str.replace("-", "")
    # print(card_str)   # check card number
    if len(card_str) == 16:
        return 1
    else:
        return 0

for test_case in range(1, int(input())+1):
    result = is_card(input())
    print(f"#{test_case} {result}")