# 1949. 등산로 조성


# solution delta-search
'''
def is_in_area(x: int, y: int, length: int):
    return 0 <= x < length and 0 <= y < length

def recursive_move(lst_:list, x: int, y: int, n: int):
    delta = [
        (0, 1), (0, -1), (1, 0), (-1, 0)
    ]
    lst_2 = []
        
    for dx, dy in delta:
        len_ = 1
        if is_in_area(x+dx, y+dy, n):
            if lst_[x][y] > lst_[x+dx][y+dy]:
                len_ += recursive_move(lst_, x+dx, y+dy, n)
        
        lst_2.append(len_)
    
    return max(lst_2)

def get_longest(lst_: list, n: int):
    max_height = max([max(lst_[i]) for i in range(n)])
    max_len = 0
    
    for i in range(n):
        for j in range(n):
            if lst_[i][j] == max_height:
                t_len = recursive_move(lst_, i, j, n)
                max_len = t_len if t_len > max_len else max_len
    
    return max_len
    
def get_longest_way_num(lst_: list, n: int, k: int):
    """
    Description:
        Get longest way in mountain
    
    Arguments:
        lst_ `list`: Area information
        k `int`: Depth that user can dig
    
    Return:
        `int`: Length of longest way
    """
    ans = 0
    
    for i in range(n):
        for j in range(n):
            for deep in range(0, k+1):
                lst_[i][j] -= deep
                
                if lst_[i][j] < 0:
                    lst_[i][j] += deep
                    break
                
                max_len = get_longest(lst_, n)
                
                ans = max_len if max_len > ans else ans
                
                lst_[i][j] += deep
    
    return ans


# input & print
for test_case in range(1, int(input()) + 1):
    length_num, depth_num = map(int, input().split())
    area_lst = [list(map(int, input().split())) for _ in range(length_num)]
    
    print(f"#{test_case}", get_longest_way_num(area_lst, length_num, depth_num))
'''

# solution - DFS
def get_graph(n: int):
    delta = [
        (0, 1), (0, -1), (1, 0), (-1, 0)
    ]
    
    graph = [[[] for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for dx, dy in delta:
                if 0 <= i+dx < n and 0 <= j+dy < n:
                    graph[i][j].append((i+dx, j+dy))
            
    return graph
    
def recursive(graph: list, lst_: list, x: int, y: int):
    len_lst = []
   
    for x2, y2 in graph[x][y]:
        len_ = 1
        if lst_[x][y] > lst_[x2][y2]:
            len_ += recursive(graph, lst_, x2, y2)
        len_lst.append(len_)
            
    return max(len_lst)

def get_longest(lst_: list, n: int, lst_2: list):
    graph = get_graph(n)
    max_len = 0
    
    # max_height = max([max(lst_[i]) for i in range(n)])
    for i, j in lst_2:
        t_len = recursive(graph, lst_, i, j)
        max_len = t_len if t_len > max_len else max_len
                
    return max_len

def get_longest_way_num(lst_: list, n: int, k: int):
    """
    Description:
        Get longest way in mountain
    
    Arguments:
        lst_ `list`: Area information
        k `int`: Depth that user can dig
    
    Return:
        `int`: Length of longest way
    """
    ans = 0
    max_height = max([max(lst_[i]) for i in range(n)])
    
    lst_2 = []
    for i in range(n):
        for j in range(n):
            if lst_[i][j] == max_height:
                lst_2.append((i, j))
    
    for i in range(n):
        for j in range(n):
            for deep in range(0, k+1):
                lst_[i][j] -= deep
                
                if lst_[i][j] < 0:
                    lst_[i][j] += deep
                    break
                
                max_len = get_longest(lst_, n, lst_2)
                
                ans = max_len if max_len > ans else ans
                
                lst_[i][j] += deep
                
    return ans

# input & print
for test_case in range(1, int(input()) + 1):
    length_num, depth_num = map(int, input().split())
    area_lst = [list(map(int, input().split())) for _ in range(length_num)]
    
    print(f"#{test_case}", get_longest_way_num(area_lst, length_num, depth_num))
    

# 질문 사항
# 높이를 깎은 후 최대 높이 봉우리들에서 출발 X
# 높이를 깎기 이전의 최대 높이 봉우리들에서 출발