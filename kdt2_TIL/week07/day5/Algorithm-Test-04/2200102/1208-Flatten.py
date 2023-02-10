# 1208. Flatten


TEST_CASE = 10
WIDTH = 100

# solution
def get_diff_max_min(lst_: list, dump: int):
    '''
    Description:
        Calculate dump moving maximum height to minimum height
    Arguments:
        lst_`list` : list of box heights
        dump`int` : dump numbers
    Returns:
        `int` : difference between maximum and minimum
    '''
    for i in range(dump):
        max_idx = lst_.index(max(lst_))
        min_idx = lst_.index(min(lst_))
        
        ans = lst_[max_idx] - lst_[min_idx]
        if ans <= 1:
            break
        
        lst_[max_idx] -= 1
        lst_[min_idx] += 1
    else:
        ans = max(lst_) - min(lst_)
    
    return ans
    

# input & print
for test_case in range(1, TEST_CASE + 1):
    dump_num = int(input())
    height_lst = list(map(int, input().split()))
    
    print(f"#{test_case}", get_diff_max_min(height_lst, dump_num))