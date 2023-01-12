# 2056. 연월일 달력
# print("\033[90mdebug![code]\033[0m")

day_31 = [1, 3, 5, 7, 8, 10, 12]
day_30 = [4, 5, 8, 11]

for T in range(1, int(input()) + 1):
    date = input()
    date_result = ""
    
    for ch in date:
        if not ('0' <= ch and ch <= '9'):
            date_result = "-1"
            break
    else:        
        month = int(date[4:6])
        day = int(date[6:])
        if month == 2:
            if not (1 <= day and day <= 28):
                date_result = "-1"
        elif month in day_31:
            if not (1 <= day and day <= 31):
                date_result = "-1"
        elif month in day_30:
            if not (1 <= day and day <= 30):
                date_result = "-1"
        else:
            date_result = "-1"
            
    if date_result == "":
        date_result += date[:4] + "/" + str(month).zfill(2) + "/" + str(day).zfill(2)
    print(f"#{T} {date_result}")