while True:
    problem_number = input('문제 번호 입력 > ')
    if problem_number == '1':
        print(f'# {problem_number}. 문자열을 입력받고, e 가 처음 나오는 위치(index)를 출력하세요. 만약, 문자열에서 e 가 없으면 -1 을 출력하세요.\n\
단, index() / find() 메서드는 사용하지마세요.')
        ########## solution code
        string = input('문자열을 입력하세요 > ')

        for i in range(len(string)):
            if string[i] == 'e':
                print(i)
                break
        else:
            print(-1)
        ##########
        print()
        
    elif problem_number == '2':
        print(f'# {problem_number}. \
문자열을 입력받고, 각 단어의 등장 횟수를 출력하세요.\n\
단, count() 메서드는 사용하지마세요.')
        ########## solution code
        strings = input("문자열을 입력하세요 > ").split()
        dict_var = {}

        for word in strings:
            dict_var[word] = dict_var.get(word, 0) + 1

        for key, value in dict_var.items():
            print(key, value)
        ##########
        print()
        
    elif problem_number == '3':
        print(f'# {problem_number}. \
문자열을 입력받고, e 를 제거한 결과를 출력하세요.\n\
단, replace() 메서드는 사용하지 마세요.')
        ########## solution code
        string = input("문자열을 입력하세요 > ")
        result = ""

        for ch in string:
            if ch != 'e':
                result += ch
        print(result)
        ##########
        print()
       
    elif problem_number == '4':
        print(f'# {problem_number}. \
문자열과 알파벳을 공백으로 구분해서 입력받고, 문자열에서 입력한 알파벳의 개수를 출력하세요.\n\
단, count() 메서드는 사용하지마세요.')
        ########## solution code
        word, alphabet = input('문자열을 입력하세요 > ').split()
        count = 0
        
        for ch in word:
            if ch == alphabet:
                count += 1
        print(count)
        ##########
        print()
        
    elif problem_number == '5':
        print(f'# {problem_number}. \
양의 정수 3개를 입력받고, 3개의 양수를 - 로 연결해서 출력하세요.\n\
단, join() 메서드는 사용하지마세요.')
        ########## solution code
        n1, n2, n3 = list(map(int, input('문자열을 입력하세요 > ').split()))

        print(str(n1).zfill(3), str(n2).zfill(4), str(n3).zfill(4), sep = '-')
        ##########
        print()
        
    elif problem_number == '6':
        print(f'# {problem_number}. \
양의 정수를 입력받고, 자리수의 합을 출력하세요. \
만약, 입력 받은 값이 0보다 작으면 -1을 출력하세요.\n\
단, 양의 정수를 문자열로 변경하지마세요. str() 함수를 사용하지마세요.')
        ########## solution code
        num = int(input("문자열을 입력하세요 > "))
        sum = 0

        if num < 0:
            sum = -1
        while num > 0:
            sum += num % 10
            num = int(num / 10)
        
        print(sum)
        ##########
        print()
     
    else:
        print('Terminated!')
        break