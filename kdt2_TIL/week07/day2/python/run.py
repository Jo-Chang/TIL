# run.py

import sys
PROBLEM_NUM = 1063
sys.stdin = open(f"{PROBLEM_NUM}.txt")

#####

 ## initialize
BOARD_SIZE = 8

movement_dict = {
    "R": (1, 0),
    "L": (-1, 0),
    "T": (0, 1),
    "B": (0, -1),
    "RT": (1, 1),
    "LT": (-1, 1),
    "RB": (1, -1),
    "LB": (-1, -1),
}

## input
# board_lst = [[0] * BOARD_SIZE for _ in range(BOARD_SIZE)]
king_pos, rock_pos, move_num = sys.stdin.readline().split()

move_lst = []
for _ in range(int(move_num)):
    move_lst.append(sys.stdin.readline().strip())
    
    
## solution
def is_in_board(n1: int, n2: int):
    '''
    # Description
    Check if piece is in board after movement
    
    argument:
        n1  : int, location of x(column)
        n2  : int, location of y(row)
    
    # return
    bool    : True if in board else False
    '''
    return True if 0 <= n1 < BOARD_SIZE and 0 <= n2 < BOARD_SIZE else False
    
def get_location(pos1: str, pos2: str, lst_: list):
    '''
    Description:
        Input location of king and rock in chess board and movements of king
    arguments:
        pos1    : `str`, location of king
        pos2    : `str`, location of rock
        lst_    : `list`, movement of king
    returns:
        `str`   : location of king as chess-format(A1 ~ H8)
        `str`   : location of rock as chess-format(A1 ~ H8)
    '''
    p1 = ("ABCDEFGH".index(pos1[0]), "12345678".index(pos1[1]))
    p2 = (ord(pos2[0]) - ord('A'), int(pos2[1]) - 1)
    
    print(p1, p2)
    
    for move in lst_:
        new = (p1[0] + movement_dict[move][0], p1[1] + movement_dict[move][1])
        new2 = p2   ## Rock stays if king doesn't touch it
        
        print(f"case : {move}")
        print(f"king move {new}, {new2}")
        
        if not is_in_board(new[0], new[1]):
            print("skip movement")
            continue
        
        ## Check rock location
        if new[0] == new2[0] and new[1] == new2[1]:
            new2 = (p2[0] + movement_dict[move][0], p2[1] + movement_dict[move][1])
            print(f"rock move {new}, {new2}")
            
            if not is_in_board(new2[0], new2[1]):
                continue
        
        p1 = new    ## Move king
        p2 = new2   ## Move rock
        # print(p1, p2)
        
    # return ("ABCDEFGH"[p1[0]]+"12345678"[p1[1]], "ABCDEFGH"[p2[0]]+"12345678"[p2[1]])
    return (chr(ord("A")+p1[0]) + str(p1[1]+1), chr(ord("A")+p2[0]) + str(p2[1]+1))
    

## print
print(*get_location(king_pos, rock_pos, move_lst), sep="\n")