# 2043. 서랍의 비밀번호

P, K = map(int, input().split())

diff = P - K
print(diff + 1 if diff > 0 else (1000 + diff) % 1000 + 1)