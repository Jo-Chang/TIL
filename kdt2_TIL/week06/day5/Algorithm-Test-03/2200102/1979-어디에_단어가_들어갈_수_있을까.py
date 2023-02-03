# 1979. 어디에 단어가 들어갈 수 있을까


# solution
def get_ans(lst2d_, n):
    ans = 0
    len_ = len(lst2d_)
    
    for i in range(len_):
        cnt = 0
        for j in range(len_):
            if lst2d_[i][j] == 1:
                cnt += 1
            else:
                if cnt == n:
                    ans += 1
                cnt = 0
            
        if cnt == n:
            ans += 1
            
    return ans
    
def get_location_num(lst2d_, n):
    lst2d_2 = list(zip(*lst2d_)) # rotate
    # pprint(lst2d_)
    # pprint(lst2d_2)
    
    return get_ans(lst2d_, n) + get_ans(lst2d_2, n)
    
    
# input, print
for test_case in range(1, int(input()) + 1):
    board_num, word_num = map(int, input().split())
    board_lst = []
    for _ in range(board_num):
        board_lst.append(list(map(int, input().split())))
    
    print(f"#{test_case}", get_location_num(board_lst, word_num))