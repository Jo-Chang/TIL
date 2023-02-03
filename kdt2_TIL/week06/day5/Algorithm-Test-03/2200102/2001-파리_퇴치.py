# 2001. 파리 퇴치


# solution
def get_max_kill_score(n, lst2d_):
    len_ = len(lst2d_)
    lst_ = []
    
    for i in range(len_ - n + 1):
        for j in range(len_ - n + 1):
            area_ = 0
            for k in range(n):
                area_ += sum(lst2d_[i+k][j:j+n])
            lst_.append(area_)
            
    return max(lst_)


# input, print
for test_case in range(1, int(input()) + 1):
    area_num, weapon_area_num = map(int, input().split())
    monster_lst = []
    for _ in range(area_num):
        monster_lst.append(list(map(int, input().split())))
    
    print(f"#{test_case}", get_max_kill_score(weapon_area_num, monster_lst))