### 아래의 리스트에서 고유한 지역의 개수는?
my_list = ['서울', '서울', '대전', '광주',
           '서울', '대전', '부산', '부산']
sets = set(my_list)

# sol_1
count = 0
for s in my_list:
    count += 1
print(f'고유한 지역의 수 : {count}')

# sol_2
count = 0
for s in sets:
   count += 1
print(f'고유한 지역의 수 : {count}') 

# sol_3
print(f'고유한 지역의 수 : {len(sets)}')

# sol_4
my_list2 = []
for i in my_list:
    if i not in my_list2:
        my_list2.append(i)
print(f'고유한 지역의 수 : {len(my_list2)}')
print(my_list2)

# sol_answer
locations = ['서울', '서울', '대전']
result = []

# 지역을 하나씩 반복
for location in locations:
    # 만약에 결과 통에 없다면,
    if location not in result:
        # 결과 통에 추가
        result.append(location)
        
print(result)
print(len(result))
print(set(locations))
print(len(set(locations)))

##################################################