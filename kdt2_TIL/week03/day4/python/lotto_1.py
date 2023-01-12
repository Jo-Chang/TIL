import random 

def get_lotto_1(n):
    # Input : 
     # n 로또 번호 세트 수
    # Output : 
     # 오늘 지른 로또 금액
     # 번호
    result = []
    for i in range(n):
         result.append(sorted(random.sample(range(1, 46), 6)))
    return result

def get_lotto_price_1(n):
    return n * 1000