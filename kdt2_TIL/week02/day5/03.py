ans = 0
berrys = []

# berry read
with open('./data/fruits.txt', 'r') as f:
    lines = f.readlines()

    for line in lines:
        if line[-6:] == 'berry\n':
            if line not in berrys:
                berrys.append(line)
                ans += 1
                
    # for line in lines:
    #     line = line.strip()
    #     if line[-5:] == 'berry':
    #         if line not in berrys:
    #             berrys.append(line)
    #             ans += 1

berrys.insert(0, str(ans) + '\n')

# 03.txt write
with open('./03.txt', 'w') as f:
    for s in berrys:
        f.write(s)