print("# 1. 숫자를 입력 받고, 10을 더해서 출력하세요.")
num1 = int(input("숫자를 입력해주세요 > "))
print(num1 + 10)
print()


print("# 2. 좋아하는 음식을 입력 받고, 출력하세요.")
food = input("좋아하는 음식을 입력해주세요 > ")
print(food)
print()


print("# 3. 이름과 태어난 년도를 입력 받고, 출력하세요. \
(단, 태어난 년도를 나이로 변환해서 출력하세요.)")
name = input("이름을 입력해주세요 > ")
year = int(input("태어난 년도를 입력해주세요 > "))
age = str(2024 - year)
print("저의 이름은 " + name + "이고, 올해 나이는 " + age + "세 입니다.")
print()

print("# 4. 문장 두 개를 입력 받고, 두 문장을 연결해서 출력하세요.")
str4_1 = input("첫 번째 문장을 입력해주세요 > ")
str4_2 = input("두 번째 문장을 입력해주세요 > ")
print(str4_1 + str4_2)
print()

print("# 5. 숫자 한 개를 입력 받고, 숫자의 부호를 바꿔서 출력하세요.")
num5 = int(input("숫자를 입력해주세요 > "))
print(-num5)
print()


print("# 6. 숫자 두 개를 입력 받고, 두 숫자에 대한 아래 산술 연산 결과를 출력하세요.")
num6_1 = int(input("첫 번째 숫자를 입력해주세요 > "))
num6_2 = int(input("두 번째 숫자를 입력해주세요 > "))
print("더하기 연산 : " + str(num6_1 + num6_2))
print("빼기 연산 : " + str(num6_1 - num6_2))
print("곱하기 연산 : " + str(num6_1 * num6_2))
print("몫 연산 : " + str(int(num6_1 / num6_2)))
print("나머지 연산 : " + str(num6_1 % num6_2))
print()


print("# 7. 숫자 세 개를 입력 받고, 세 숫자의 평균을 출력하세요.")
num7_1 = int(input("첫 번째 숫자를 입력해주세요 > "))
num7_2 = int(input("두 번째 숫자를 입력해주세요 > "))
num7_3 = int(input("세 번째 숫자를 입력해주세요 > "))
average = int((num7_1 + num7_2 + num7_3) / 3)
print(average)
print()

print("# 8. 숫자 다섯 개를 입력 받고, 다섯 개의 숫자를 리스트 객체에 저장해서 출력하세요.")
list8 = []
list8.append(int(input("첫 번째 숫자를 입력해주세요 > ")))
list8.append(int(input("두 번째 숫자를 입력해주세요 > ")))
list8.append(int(input("세 번째 숫자를 입력해주세요 > ")))
list8.append(int(input("네 번째 숫자를 입력해주세요 > ")))
list8.append(int(input("다섯 번째 숫자를 입력해주세요 > ")))
print(list8)
print()

print("# 9. 문자열 하나와 숫자 한 개를 입력 받고, 문자열을 숫자만큼 반복해서 출력하세요.")
str9 = input("문자열을 입력해주세요 > ")
num9 = int(input("숫자를 입력해주세요 > "))
print(str9 * num9)
print()


print("# 10. 숫자 다섯 개를 입력 받고, 입력할 때 마다 입력한 숫자들의 합을 출력하세요.")
num10 = int(input("첫 번째 숫자를 입력해주세요 > "))
print(num10)
num10 += int(input("두 번째 숫자를 입력해주세요 > "))
print(num10)
num10 += int(input("세 번째 숫자를 입력해주세요 > "))
print(num10)
num10 += int(input("네 번째 숫자를 입력해주세요 > "))
print(num10)
num10 += int(input("다섯 번째 숫자를 입력해주세요 > "))
print(num10)