locations = ['서울', '서울', '대전', '부산', '대전']

# 지역별 갯수를 구하세요.
# {'서울': 2, '대전': 2, '부산: 1}
result = {}
for location in locations:
    # 만약에 result에 없으면 키 값 추가
    if location not in result:
        result[location] = 1
    # result에 있으면 값 추가
    else:
        result[location] += 1
        
print(result)

#######################################################
locations.clear()
result.clear()
#######################################################
locations = ['서울', '서울', '대전', '부산', '대전']

# 지역별 갯수를 구하세요.
# {'서울': 2, '대전': 2, '부산: 1}
result = {}
for location in locations:
    # 만약에 result에 없으면 키 값 추가
    # result에 있으면 값 추가
    result[location] = result.get(location, 0) + 1
    
print(result)