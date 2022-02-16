import heapq
import sys

input = sys.stdin.readline
n = int(input())

pq = []
#arr = []

for i in range(n):
    a = int(input())
    #arr.append(a)
    if a == 0:
        if pq:
            # pq에 값이 있으면
            print(heapq.heappop(pq)[1])
        else:
            print("0")
    else:
        heapq.heappush(pq ,[-a, a])

