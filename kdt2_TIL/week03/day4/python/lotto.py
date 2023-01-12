import random

'''
numbers = range(1, 46)
# random.sample()
lucky = sorted(random.sample(numbers, 6))
print(lucky)
'''

def get_lotto(n):
    # Input : 
     # n 로또 번호 세트 수
    # Output : 
     # 오늘 지른 로또 금액
     # 번호
    result = []
    for i in range(n):
         result.append(sorted(random.sample(range(1, 46), 6)))
    return result

'''
NUM_OF_LOTTO = 2
print(get_lotto(2))
print(f"get_lotto_price(2)원")
'''