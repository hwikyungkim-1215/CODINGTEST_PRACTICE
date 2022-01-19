K, N = map(int, input().split())
arr = []
sum = 0
for _ in range(K):
    arr.append(int(input()))

arr.sort()
start = 1
end = max(arr)

# 이분 탐색(상한)
while start <= end:
    # 매번 초기회
    count = 0
    mid = (start+end) // 2
    # mid로 각 나무 자른 개수 합
    for i in arr:
        count += i // mid

    # 자른 나무 개수가 많으면 mid 늘리기
    if count >= N:
        start = mid + 1
    # 자른 나무 개수가 적으면 mid 줄이기
    else:
        end = mid - 1

print(end)