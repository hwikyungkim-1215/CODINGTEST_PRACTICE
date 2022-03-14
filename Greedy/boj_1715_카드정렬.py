# 힙 이용 안하면 시간초과
import sys
import heapq
input = sys.stdin.readline

n = int(input())
# 우선순위 큐 이용
li = heapq
result = []

for _ in range(n):
    li.heappush(result, int(input()))
#print("li", li)

if len(result) == 1:
    print(0)
else:
    sum = 0
    while len(result) > 1:
        temp1 = li.heappop(result)
        temp2 = li.heappop(result)
        sum += temp1 + temp2
        heapq.heappush(result, temp1 + temp2)
    print(sum)

