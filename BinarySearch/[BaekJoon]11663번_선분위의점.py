'''
이진 검색 (Binary Search): bisect_left / bisect_right
bisect_left(a, x) #하한
정렬된 a에 x를 삽입할 위치를 리턴해준다. x가 a에 이미 있으면 기존 항목의 앞 (왼쪽)의 위치를 반환한다.

bisect_right(a, x) # 상한
bisect_left와 거의 같은 함수인데, 이번에는 x가 a에 이미 있으면 기존 항목 뒤 (오른쪽)의 위치를 반환한다.
'''

from bisect import bisect_left, bisect_right
import sys

input = sys.stdin.readline
N, M = map(int, input().rstrip().split())
arr = list(map(int, input().split()))
arr.sort()

for _ in range(M):
    # 입력받은 두 점 이진탐색
    a, b = map(int, input().rstrip().split())
    #0 3
    start_num = bisect_left(arr, a)
    end_num = bisect_right(arr, b)

    print(end_num - start_num)


'''
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
'''