# 10505. 소득 불균형
import sys

sys.stdin = open("10505_소득_불균형.txt")

##########

def get_under_num(incomes):
    # under_mean = 0
    # for income in incomes:
    #     if income <= sum(incomes) / len(incomes):
    #         under_mean += 1
    # return under_mean
    return len([income for income in incomes if income <= sum(incomes) // len(incomes)])

for test_case in range(1, int(input()) + 1):
    people_num = int(input())
    answer = get_under_num(list(map(int, input().split())))
    print(f"#{test_case} {answer}")