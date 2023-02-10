# 11856. 반반

# solution
def is_half_half(word: str):
    '''
    Description:
        Judge two alphabet * 2
    
    Arguments:
        word`str`: string to judge
    
    Return:
        Return "Yes" if there is two alphabet * 2 else "No"
    '''
    dict_ = {}
    for c in word:
        dict_[c] = dict_.get(c, 0) + 1
        # Judge word has a alphabet three times
        if dict_[c] > 2:
            return "No"
    
    # Judge word has more than two alphabets
    if len(dict_) > 2:
        return "No"
    else:
        return "Yes"


# input & print
for test_case in range(1, int(input()) + 1):
    word = input()
    print(f"#{test_case}", is_half_half(word))