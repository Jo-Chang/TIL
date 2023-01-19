def print_problem_info(str1, str2):
    print(f"\033[95m# {str1}. \x1b[96m{str2}\033[00m")

list_var = [0 for i in range(6)]
list_var = [2789, 2675, 10988, 17249, 2941, 10809]
dict_var = {
    list_var[0] : "유학 금지",
    list_var[1] : "문자열 반복",
    list_var[2] : "팰린드롬인지 확인하기",
    list_var[3] : "태보태보 총난타",
    list_var[4] : "크로아티아 알파벳",
    list_var[5] : "알파벳 찾기",
}

dict_var = dict(sorted(dict_var.items()))

while True:
    print("===아래 리스트에서 문제 번호 선택!===")
    for k, v in dict_var.items():
        print(f"\u001b[90m{k}. {v}\033[0m")

    try:
        problem_num = int(input("\n문제 번호 입력 > "))
    except:
        print("Terminated!")
        break
    
    if problem_num == list_var[0]:
        print_problem_info(problem_num, dict_var[problem_num])
        #################### solution code
        restrict = "CAMBRIDGE"
        word = input()

        for i_char in word:
            if i_char not in restrict:
                print(i_char, end="")
        ####################
    
    elif problem_num == list_var[1]:
        print_problem_info(problem_num, dict_var[problem_num])
        #################### solution code
        for test_case in range(1, int(input()) + 1):
            repeat_num, word = input().split()
            repeat_num = int(repeat_num)
            
            for i_char in word:
                print(i_char * repeat_num, end="")
            print()
            # print(*[i_char*repeat_num for i_char in word], sep="")
        ####################
    
    elif problem_num == list_var[2]:
        print_problem_info(problem_num, dict_var[problem_num])
        #################### solution code
        def is_palindrome(word):
            for i in range(len(word) // 2 + 1):
                if (word[i] == word[-1 - i]):
                    pass
                else:
                    return 0
            return 1
        
        def is_palindrome2(word):
            if (word == word[::-1]):
                return 1
            else:
                return 0
            
        def is_palindrome3(word):
            i = 0
            rev_i = len(word) - 1 - i
            while i < len(word) - 1 - i:
                if word[i] != word[len(word) - 1 - i]:
                    return 0
                i += 1
            else:
                return 1
            
        print(is_palindrome(input()))
        ####################
    
    elif problem_num == list_var[3]:
        print_problem_info(problem_num, dict_var[problem_num])
        #################### solution code
        taebo_input = input()

        face_index = taebo_input.find("(^0^)")
        left_num = 0
        right_num = 0

        for index in range(face_index):
            if taebo_input[index] == "@":
                left_num += 1
                
        for index in range(face_index, len(taebo_input)):
            if taebo_input[index] == "@":
                right_num += 1

        print(left_num, right_num)
        # print(taebo_input[:face_index].count("@"), taebo_input[face_index:].count("@"))
        ####################
    
    elif problem_num == list_var[4]:
        print_problem_info(problem_num, dict_var[problem_num])
        #################### solution code
        word_input = input()

        chro_alphabet = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
        word_len = len(word_input)
        for alphabet in chro_alphabet:
            word_len -= word_input.count(alphabet)

        print(word_len)
        ####################
    
    elif problem_num == list_var[5]:
        print_problem_info(problem_num, dict_var[problem_num])
        #################### solution code
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        word = input()

        list_index = []
        for i_char in alphabet:
            list_index.append(word.find(i_char))
        print(*list_index)
        ####################
        
    else:
        print("Terminated!")
        break

    print()