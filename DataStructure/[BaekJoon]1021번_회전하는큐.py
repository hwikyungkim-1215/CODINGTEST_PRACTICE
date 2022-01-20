from collections import deque
import sys
input = sys.stdin.readline
N, M = map(int, input().split())

b = []
A = []

# 처음 리스트
arr = deque([i+1 for i in range(N)])

# 삭제할 수 위치
deletes = list(map(int,input().split()))
result = 0

for number in deletes:
    while True:
        # 먼저 삭제 할 수랑 같으면 삭제 후 break
        if arr[0] == number:
            arr.popleft()
            break
        else:
            # number의 인덱스 찾기
            for i in range(len(arr)):
                if arr[i] == number:
                    # 앞 거리
                    count = i
                    # 뒤 거리
                    count2 = len(arr)-count
                    break
            # 왼쪽이 더 가까운 경우
            if count < count2:
                for i in range(count):
                    # arr.rotate(-1)
                    arr.append(arr.popleft())
                result += count

            # 오른 쪽이 더 가까운 경우
            else:
                for i in range(count2):
                    # arr.rotate(1)
                    arr.appendleft(arr.pop())
                result += count2

print(result)
