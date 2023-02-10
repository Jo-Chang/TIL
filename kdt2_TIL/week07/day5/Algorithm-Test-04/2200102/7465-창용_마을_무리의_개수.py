# 7465. 창용 마을 무리의 개수

NOT_VISITED = False
VISITED = True

# solution
def get_adjacency_num(graph: list, v: int, e: int):
    ''' 
    Description:
        Calculate how many relations(path) in the town(graph)
    
    Arguments:
        graph`list`: relation of people in town
        v`int`: people num
        e`int`: relation between people num
    
    Return:
        `int`: number of relations(path) in town(graph)
    '''
    visited = [NOT_VISITED] * (v + 1)
    stack = []
    ans = 0
    
    for i in range(1, v+1):
        if visited[i]:
            continue
        ans += 1
        
        stack.append(i)
        visited[i] = VISITED
        
        while stack:
            num = stack.pop()
            
            for adj in graph[num]:
                if not visited[adj]:
                    stack.append(adj)
                    visited[adj] = VISITED
    
    return ans


# input & print
for test_case in range(1, int(input()) + 1):
    vertex_num, edge_num = map(int, input().split())
    
    # Init graph
    graph_lst = [[] for _ in range(vertex_num + 1)]
    # Add to graph
    for _ in range(edge_num):
        v1_num, v2_num = map(int, input().split())        
        graph_lst[v1_num].append(v2_num)
        graph_lst[v2_num].append(v1_num)
    
    print(f"#{test_case}", get_adjacency_num(graph_lst, vertex_num, edge_num))