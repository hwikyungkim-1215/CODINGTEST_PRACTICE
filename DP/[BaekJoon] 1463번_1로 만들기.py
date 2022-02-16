n = int(input())
# 이전에 구한 값 저장
dp = [0] * (n+1)

# DP
for i in range(2, n+1):
    # 현재의 수에서 1빼는 경우
    dp[i] = dp[i-1] + 1
    # 현재의 수가 3로 나누어 떨어지는 경우
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3] + 1)
    # 현재의 수가 2로 나누어 떨어지는 경우
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2] + 1)

print(dp[n])