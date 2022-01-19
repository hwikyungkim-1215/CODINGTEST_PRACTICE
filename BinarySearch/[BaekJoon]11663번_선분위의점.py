import sys

input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
result = []

for _ in range(M):
    start, end = map(int, input().split())
    for i in range(1, M):
        if start < arr[i]:
            start_num = i
            break
        else:
            start_num = M
    for j in range(1, M):
        if end < arr[j]:
            end_num = j
            break
        else:
            end_num = M

    if start == arr[start_num - 1]:
        a = end_num - start_num + 1
        result.append(a)
    else:
        b = end_num - start_num
        result.append(b)

for i in range(M):
    print(result[i])