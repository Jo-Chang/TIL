# 4406. 모음이 보이지 않는 사람

# solution
def get_vowel_removed(word: str):
    ''' 
    Description:
        Get word of which vowel is removed
    
    Arguments:
        word`str`: input word which only has lower alphabet
    
    Return:
        `str`: word which is removed vowel from original word
    '''
    vowels = ['a', 'e', 'i', 'o', 'u']
    
    for c in vowels:
        word = word.replace(c, "")
        
    return word


# input & print
for test_case in range(1, int(input()) + 1):
    word = input()
    
    print(f"#{test_case}", get_vowel_removed(word))