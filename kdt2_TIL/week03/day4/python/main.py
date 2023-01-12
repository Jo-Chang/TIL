from lotto import get_lotto
from lotto_1 import get_lotto_1, get_lotto_price_1
from lotto_oop import Lotto

NUM_OF_LOTTO = 5

# 버전 1
print(get_lotto(NUM_OF_LOTTO))

# 버전 2
print(get_lotto_1(NUM_OF_LOTTO))
print(get_lotto_price_1(NUM_OF_LOTTO))

# OOP 버전
l = Lotto(5)
print(*l.lotto_numbers, sep = "\n")
print("]")
l.update_numbers()
print(*l.lotto_numbers, sep = "\n")
print(l.pprint())