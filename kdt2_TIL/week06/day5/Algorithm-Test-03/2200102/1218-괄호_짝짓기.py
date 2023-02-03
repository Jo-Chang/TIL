# 1218. 괄호 짝짓기


# solution
def is_correct_word(word):
    dict_ = {
        "{" : "}",
        "(" : ")",
        "[" : "]",
        "<" : ">",
    }
    
    lst_2 = []
    for ch in word:
        if ch in "{[(<":
            lst_2.append(ch)
        elif ch in "}])>":
            if dict_[lst_2.pop()] != ch:
                return 0
    
    if lst_2:
        return 0
    else:
        return 1
        
    
# input, print
TEST_CASE = 10

for test_case in range(1, TEST_CASE + 1):
    word_len = int(input())
    word_lst = input()
    
    print(f"#{test_case}", is_correct_word(word_lst))