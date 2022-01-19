import sys

input = sys.stdin.readline
n, m = map(int, input().split())
h = list(map(int, input().split())) #나무 높이

start = 1
end = max(h)

# 이분 탐색(상한)
while start <= end:
    mid = (start+end) // 2
    sum = 0 # 벌목된 나무 길이 합계
    for i in h:
        if i > mid:
            sum += (i-mid) #벌목 추가

    if sum >= m: # 합계가 크면 자르는 높이H 증가
        start = mid + 1
    else:
        end = mid - 1

print(end)