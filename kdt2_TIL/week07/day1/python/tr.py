import sys


def print_problem_info(str1, str2):
    print(f"\033[95m# {str1}. \x1b[96m{str2}\033[00m")


list_var = [0 for i in range(6)]
list_var = [10769, 2455, 2606, 4963]
dict_var = {
    list_var[0] : "행복한지 슬픈지",
    list_var[1] : "지능형 기차",
    list_var[2] : "바이러스",
    list_var[3] : "섬의 개수",
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
        # input
        message = sys.stdin.readline().strip()
            

        # solution
        def get_mood(message):
            happy_num = message.count(":-)")   # count smile emotion
            sad_num = message.count(":-(")     # count sad emotion
            
            if happy_num == sad_num == 0:   # no emotion in msg
                return "none"
            elif happy_num == sad_num:      # same emotion counts
                return "unsure"
            elif happy_num > sad_num:       # smile emotions greater
                return "happy"
            else:                           # sad emotions greater
                return "sad"

        # print
        print(get_mood(message))
        ####################
    
    
    
    
    
    elif problem_num == list_var[1]:
        print_problem_info(problem_num, dict_var[problem_num])
        
        
        #################### solution code
        STATION_NUM = 4

        # input
        num_people_lst = []
        for _ in range(STATION_NUM):
            get_off_num, get_on_num = map(int, sys.stdin.readline().split())
            num_people_lst.append((get_off_num, get_on_num))    # tuple in list
            

        # solution
        def get_max_people_num(lst_):
            num = 0
            max_num = 0
            
            for off, on in lst_:
                num += on - off
                if num > max_num:   
                    max_num = num   # Renew maximun number of 'people in train'
                    
            return max_num    


        # print
        print(get_max_people_num(num_people_lst))
        ####################
    
    
    
    
    
    elif problem_num == list_var[2]:
        print_problem_info(problem_num, dict_var[problem_num])
        
        
        #################### solution code
        VIRUS_ROOT = 1  # 1번 컴퓨터 바이러스

        # input vertex, edge
        vertex_num = int(sys.stdin.readline())
        edge_num = int(sys.stdin.readline())

        # make grpah
        graph_lst = [[] for _ in range(vertex_num + 1)]

        # input edge information
        for _ in range(edge_num):
            edge1, edge2 = map(int, sys.stdin.readline().split())
            graph_lst[edge1].append(edge2)
            graph_lst[edge2].append(edge1)
            

        # solution
        def get_infected_num(graph_, n):
            lst_ = []
            visited = [False]  * len(graph_)
            
            # dfs
            lst_.append(n)
            
            while lst_:
                cur = lst_.pop()
                visited[cur] = True
                
                # adjacent vertex
                for adj in graph_[cur]:
                    if not visited[adj]:
                        lst_.append(adj)
            
            return len([mem for mem in visited if mem]) - 1

        print(graph_lst)
        
        # print
        print(get_infected_num(graph_lst, VIRUS_ROOT))
        ####################
    
    
    
    
    
    elif problem_num == list_var[3]:
        print_problem_info(problem_num, dict_var[problem_num])
        
        
        #################### solution code
        SEA = 0
        LAND = 1
        VISITED = 2


        # solution
        def find_land(lst2d_, stack):
            height = len(lst2d_)
            width = len(lst2d_[0])
            delta = [
                (-1, 0), (1, 0), (0, -1), (0, 1),
                (-1, -1), (-1, 1), (1, -1), (1, 1)
            ]
            
            while stack:
                x, y = stack.pop()
                for dx, dy in delta:
                    x2 = x + dx
                    y2 = y + dy
                    if (x2 < 0) or (x2 >= height) or (y2 < 0) or (y2 >= width):
                        # Finding out of area
                        continue    # Skip
                    
                    if lst2d_[x2][y2] == LAND:
                        stack.append((x2, y2))
                        lst2d_[x2][y2] = VISITED  # Check visited land
                        

        def get_land_num(lst2d_):
            ans = 0
            height = len(lst2d_)
            width = len(lst2d_[0])
            
            for i in range(height):
                for j in range(width):
                    stack = []
                    if lst2d_[i][j] == LAND:   # Land not visited
                        stack.append((i, j))
                        lst2d_[i][j] = VISITED    # Check visited land
                        find_land(lst2d_, stack)
                        ans += 1
                    
            return ans


        # input & print
        while True:
            width_num, height_num = map(int, sys.stdin.readline().split())
            if width_num == height_num == 0:    # End condition
                break
            
            # Input map shape
            map_shape_lst = []
            for _ in range(height_num):
                map_shape_lst.append(list(map(int, sys.stdin.readline().split())))
            
            print(map_shape_lst)
            print(get_land_num(map_shape_lst))
        ####################
        
        
        
        
        
    else:
        print("Terminated!")
        break


    print()