# 1063. 킹

import sys
PROBLEM_NUM = 1063
sys.stdin = open(f"{PROBLEM_NUM}.txt")

#####

import sys


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

# input
board_lst = [[0] * BOARD_SIZE for _ in range(BOARD_SIZE)]
king_pos, rock_pos, move_num = sys.stdin.readline().split()

move_lst = []
for _ in range(int(move_num)):
    move_lst.append(sys.stdin.readline().strip())
    
    
# solution
def is_in_board(n1, n2):
    # Check if piece is in board after movement
    return True if 0 <= n1 < BOARD_SIZE and 0 <= n2 < BOARD_SIZE else False
    
def get_location(pos1, pos2, lst_):
    p1 = ("ABCDEFGH".index(pos1[0]), "12345678".index(pos1[1]))
    p2 = (ord(pos2[0]) - ord('A'), int(pos2[1]) - 1)
    
    # print(p1, p2)
    for move in lst_:
        new = (p1[0] + movement_dict[move][0], p1[1] + movement_dict[move][1])
        new2 = p2   # Rock stays if king doesn't touch it
        
        if not is_in_board(new[0], new[1]):
            continue
        
        # Check rock location
        if new[0] == new2[0] and new[1] == new2[1]:
            new2 = (p2[0] + movement_dict[move][0], p2[1] + movement_dict[move][1])
            
            if not is_in_board(new2[0], new2[1]):
                continue
        
        p1 = new    # Move king
        p2 = new2   # Move rock
        # print(p1, p2)
        
    return ("ABCDEFGH"[p1[0]]+"12345678"[p1[1]], "ABCDEFGH"[p2[0]]+"12345678"[p2[1]])
    

# print
print(*get_location(king_pos, rock_pos, move_lst), sep="\n")