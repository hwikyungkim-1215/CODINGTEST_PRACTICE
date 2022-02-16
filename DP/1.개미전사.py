n = int(input())
# 식량 정보
li = list(map(int, input().split()))

# 앞서 계산된 결과 저장 DP
d = [0] * 100

d[0] = li[0]
d[1] = max(li[1], li[0])

# DP(보텀업)
for i in range(2,n):
    d[i] = max(li[i-1], li[i-2] + li[i])

print(d[n-1])