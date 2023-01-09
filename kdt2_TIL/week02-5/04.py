with open('./data/fruits.txt', 'r') as f:
    lines = f.readlines()
    dict_var = {}
    
    for line in lines:
        line = line.strip()
        dict_var[line] = dict_var.get(line, 0) + 1
        
with open('./04.txt', 'w') as f:
    for key, values in dict_var.items():
        f.write(f'{key} {values}\n')