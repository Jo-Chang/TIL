dict_var = {
    '1938' : '아주 간단한 계산기',
    '2029' : '몫과 나머지 출력하기',
    '2046' : '스탬프 찍기',
    '2068' : '최대수 구하기',
    '2071' : '평균값 구하기',
}

while True:
    print('===아래 리스트에서 문제 번호 선택!===')
    for k, v in dict_var.items():
        print(f'\033[95m{k}. \x1b[96m{v}')

    problem_num = input('\n\u001b[00m> ')
    
    if problem_num == '1938':
        print(f'\033[95m#{problem_num}. \033[96m{dict_var[problem_num]}\033[00m')
        #################### solution code
        a, b = map(int, input().split())

        print(a + b)
        print(a - b)
        print(a * b)
        print(a // b)
        # for e in [a + b, a - b, a * b, a // b]:
        #     print(e)
        ####################
        print()
    
    elif problem_num == '2029':
        print(f'\033[95m#{problem_num}. \033[96m{dict_var[problem_num]}\033[00m')
        #################### solution code
        T = int(input('Testcase : '))
        for test_case in range(1, T + 1):
            a, b = map(int, input().split())
            div, mod = divmod(a, b)
            print(f'#{test_case} {div} {mod}')
        ####################
        print()
    
    elif problem_num == '2046':
        print(f'\033[95m#{problem_num}. \033[96m{dict_var[problem_num]}\033[00m')
        #################### solution code
        num = int(input())

        for i in range(num):
            print('#', end = '')
            
        # print('#' * int(input()))
        ####################
        print()
    
    elif problem_num == '2068':
        print(f'\033[95m#{problem_num}. \033[96m{dict_var[problem_num]}\033[00m')
        #################### solution code
        T = int(input())
        for test_case in range(1, T + 1):
            numbers = list(map(int, input().split()))
            
            print(f'#{test_case} {max(numbers)}')
        ####################
        print()
    
    elif problem_num == '2071':
        print(f'\033[95m#{problem_num}. \033[96m{dict_var[problem_num]}\033[00m')
        #################### solution code
        T = int(input())
        for test_case in range(1, T + 1):
            numbers = map(int, input().split())
            print(f'#{test_case} {round(sum(numbers) / len(numbers))}')
        ####################
        print()
    
    else:
        print('Terminated!')
        break
