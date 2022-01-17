import sys
input = sys.stdin.readline
N = int(input())

cost = list(map(int, input().split()))
M = int(input())
start, end = 0, max(cost)
ytr
# 이분 탐색
while start <= end:
    mid = (start+end) // 2
    sum = 0 # 총 지출
    for i in cost:
        if i > mid:
            sum += mid
        else:
            sum += i
    if sum <= M:
        start = mid + 1
    else:
        end = mid -1

print(end)

