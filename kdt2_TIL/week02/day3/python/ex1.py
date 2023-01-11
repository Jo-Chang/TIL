while True:
    num = input('문제 번호 입력 > ')
    if num == '1':
        print('# 1. ')
        ### training code
        list_variable = [0, 1, 2, 3, 4, 5, 6]
        list_variable.pop()
        list_variable.append(7)
        list_variable.append(8)

        for element in list_variable[2:]:
            print(element, end=" ")
            
        """
        예측을 작성하세요.
        2 3 4 5 7 8
        """
        ###
        print()
    elif num == '2':
        print('# 2. ')
        ### training code
        for element in range(-2, 10, 2):
            print(element, end=" ")
            
        """
        예측을 작성하세요.
        -2 0 2 4 6 8
        """
        ###
    elif num == '3':
        print('# 3. ')
        ### training code
        a, b, c, d = 0, 0, 0, 0
        n = 10

        for number in range(n):
            if number % 2 == 0:
                a = a + 1
                
            if number % 3 == 0:
                b = b + 1
                
            if number % 4 == 0:
                c = c + 1
                
            if number % 5 == 0:
                d = d + 1

        print(a, b, c, d) # 5 4 3 2          
        ###
    elif num == '4':
        print('# 4. ')
        ### training code
        i = 0
        while i <= 10:
            print(i)
            i = i + 1
        """
        예측을 작성하세요.
        0
        1
        2
        3
        4
        5
        6
        7
        8
        9
        10
        """
        ###
    elif num == '5':
        print('# 5. ')
        ### training code
        i = 0
        while i <= 10:
            i = i + 1
            print(i)
        """
        예측을 작성하세요.
        1
        2
        3
        4
        5
        6
        7
        8
        9
        10
        11
        """
        ###
    elif num == '6':
        print('# 6. ')
        ### training code
        i = 0
        while i <= 10:
            i = i + 2
            print(i)
        """
        예측을 작성하세요.
        2
        4
        6
        8
        10
        12
        """
        ###
    elif num == '7':
        print('# 7. ')
        ### training code
        i = 0
        while True:
            print(i) 
            i = i + 1
            if i > 10:
                break
        """
        예측을 작성하세요.
        0
        1
        2
        3
        4
        5
        6
        7
        8
        9
        10
        """
        ###
    elif num == '8':
        print('# 8. ')
        ### training code
        i = 0
        while True:
            print(i) 
            if i > 10:
                break
            i = i + 1
            
        """
        예측을 작성하세요.
        0
        1
        2
        3
        4
        5
        6
        7
        8
        9
        10
        11
        """
        ###
    elif num == '9':
        print('# 9. ')
        ### training code
        list_variable = [0, 1, 2, 3, 4, 5, 6]
        print(len(list_variable)) # 7
        ###
    elif num == '10':
        print('# 10. ')
        ### training code
        list_variable = [0, 1, 2, 3, 4, 5, 6]
        print(sum(list_variable)) # 21
        ###
    elif num == '11':
        print('# 11. ')
        ### training code
        list_variable = [3, 1, 4, -3, 9, 7]
        print(min(list_variable) - max(list_variable)) # -12
        ###
    else:
        print('Terminated!')
        break