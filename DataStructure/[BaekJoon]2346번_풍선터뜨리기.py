from collections import deque
import sys

input = sys.stdin.readline
N = int(input())
# [(0, 3), (1, 2), (2, 1), (3, -3), (4, -1)] 으로 저장
arr = deque(enumerate(map(int, input().split())))
result = []

while True:
    # 0, 3
    index, count = arr.popleft()
    # 1
    result.append(index+1)

    if not arr:
        break
    # 오른 쪽으로 이동
    if count > 0:
        arr.rotate(-(count-1))
    # 왼쪽으로 이동
    else:
        arr.rotate(-count)

# 띄어쓰기 형태로 출력
print(' '.join(map(str, result)))
