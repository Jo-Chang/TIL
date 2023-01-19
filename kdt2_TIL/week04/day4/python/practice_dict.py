import sys

###########

while True:
    try:
        sys.stdin.flush()
        num = int(input())
    except EOFError:
        print("EOF!")
        break

    sys.stdin = open(f"practice_dict_0{num}.txt")
    if num == 1:
        pass
    elif num == 2:
        pass
    elif num == 3:
        members = input().split()
        dict_var = {}

        for member in members:
            dict_var[member] = dict_var.get(member, 0) + 1

        min_foul = min(dict_var.values())

        for key in dict_var.keys():
            if dict_var.get(key) == min_foul:
                print(key)
        print(min_foul)
        
    else:
        print("Terminated")
        break
