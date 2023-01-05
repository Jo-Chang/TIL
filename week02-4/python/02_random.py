# ""모듈""을 가져오는 것
import random

menu = ['햄버거', '국밥', '초밥']
print(random.choice(menu))

# random.sample(population, k)
# Return a k length list    6개 숫자
# the population sequence.  1~45개 숫자 중 
print('random sample : ', end = ' ')
lucky_num = random.sample(range(1, 46), 6) # 비복원 숫자이기 때문에 중복 X
print(lucky_num)
print('sort it       : ', end = ' ')
print(sorted(lucky_num))


#####

students = ['민옥', '홍엽', '현석', '정은']
print(students)
random.shuffle(students)
print(students)