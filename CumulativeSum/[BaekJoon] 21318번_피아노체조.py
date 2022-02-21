import sys

input = sys.stdin.readline
# 악보 개수
n = int(input())

# 난이도
level = list(map(int, input().split()))

# 질문 개수
#q = int(input())

dp = [0] * n
for i in range(n):
    if level[i-1] > level[i]: # 실수 할 경우
        dp[i] = dp[i-1] + 1 # 누적
    else:
        dp[i] = dp[i-1]
print(dp)

for i in range(int(input())):
    a, b = map(int, input().split())
    print(dp[b-1] - dp[a-1])




