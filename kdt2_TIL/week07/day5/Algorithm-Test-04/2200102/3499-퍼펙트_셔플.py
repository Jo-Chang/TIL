# 3499. 퍼펙트 셔플


# solution
def get_perfect_shuffle(lst_: list):
    ''' 
    Description:
        Get cards order with perfect shuffle
    
    Arguments:
        lst_`list`: cards list
    
    Return:
        `list`: cards list shuffled
    '''
    ans = []
    len_ = len(lst_)
    half = len_ // 2 if len_ % 2 == 0 else len_ // 2 + 1
    
    for i in range(len(lst_)):
        if i % 2 == 0:
            ans.append(lst_[:half][i // 2])
        else:
            ans.append(lst_[half:][i // 2])
            
    
    return ans


# input & print
for test_case in range(1, int(input()) + 1):
    words_num = int(input())
    words_lst = input().split()
    
    print(f"#{test_case}", *get_perfect_shuffle(words_lst))