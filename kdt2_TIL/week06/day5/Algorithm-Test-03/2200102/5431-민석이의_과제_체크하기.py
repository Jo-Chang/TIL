# 5431. 민석이의 과제 체크하기
# import sys


# solution
def get_not_submit_student(n, lst_):
    return [num for num in range(1, n+1) if num not in lst_]


# input, print
for test_case in range(1, int(input()) + 1):
    students_num, submit_num = map(int, input().split())
    submit_lst = list(map(int, input().split()))
    print(f"#{test_case}", *get_not_submit_student(students_num, submit_lst))