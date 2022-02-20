import sys

input = sys.stdin.readline
n, m = map(int, input().split())
t = sorted(list(int(input()) for _ in range(n)))

start = 0
end = min(t) * m #가장 긴 시간
result = 0

# 이분 탐색
while start <= end:
    mid = (start+end) // 2
    peopleNum = 0 # 사람 수
    for i in t:
        peopleNum += mid//t #사람 수

        if  peopleNum < m: # 주어진 사람 수 보다 작으면
            start = mid + 1
        else:
            result = mid
            end = mid - 1

print(result)