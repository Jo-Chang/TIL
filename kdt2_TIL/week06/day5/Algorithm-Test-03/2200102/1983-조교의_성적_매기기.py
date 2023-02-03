# 1983. 조교의 성적 매기기


# solution
def get_score(n, lst2d_):
    len_ = len(lst2d_)
    lst_ = []
    rate = [7, 9, 4]
    score_lst = ["A+", "A0", "A-", "B+", "B0", "B-", "C+", "C0", "C-", "D0"]
    
    for i in range(len_):
        score = 0
        for j in range(3):
            score += lst2d_[i][j] * rate[j]
        lst_.append(score)
        if i == n-1:
            k_score = score
            
    lst_ = sorted(lst_, reverse=True)
    
    for i in range(len_):
        if lst_[i] == k_score:
            return score_lst[i // (len_//10)]
    


# input, print
for test_case in range(1, int(input()) + 1):
    students_num, k_num = map(int, input().split())
    score_num_lst = []
    for _ in range(students_num):
        score_num_lst.append(list(map(int, input().split())))
    
    print(f"#{test_case}", get_score(k_num, score_num_lst))