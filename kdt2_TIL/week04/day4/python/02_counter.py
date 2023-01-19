from collections import Counter

print(Counter('hello apple hi'))
print(Counter('pen pineapple apple pen').most_common())
print(Counter('hello apple hi').most_common(2))