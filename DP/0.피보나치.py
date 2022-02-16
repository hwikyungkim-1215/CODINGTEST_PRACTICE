# 피보나치 함수를 재귀 함수로 구현
def fibo(x):
    if x == 1 or x == 2:
        return 1
    return fibo(x-1) + fibo(x-2)

print(fibo(4))

# 피보나치 수열 코드(재귀적)
# 한 번 계산된 결과를 메모이제이션하기 위한 리스트 초기화
dp = [0] * 100

# 피보나치 함수를 재귀함수로 구현
def fibo2(x):
    # 종료 조건
    if x == 1 or x == 2:
        return 1
    # 이미 계산한 적 있는 문제라면 그대로 반환
    if dp[x] != 0:
        return dp[x]
    # 아직 계산하지 않은 문제라면 점화식에 따라서 피보나치 결과 반환
    dp[x] = fibo2(x-1) + fibo2(x-2)
    return dp[x]

print(fibo2(4))


# 피보나치 함수를 재귀함수로 구현(보텀업 방식 - 반복문)
# 앞에서 계산된 결과를 저장하기 위한 DP 테이블 초기화
dp = [0] * 100

# 첫 번째 피보나치 수와 두 번째 피보나치 수는 1
dp[1] = 1
dp[2] = 1
n = 4

for i in range(3, n+1):
    dp[i] =  dp[i-1] + dp[i - 2]

print(dp[n])