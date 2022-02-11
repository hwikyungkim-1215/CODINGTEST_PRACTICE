import sys

n = int(input())
m = int(input())

# Inf의 범위가 작으면 틀릴 수 있 ???
Inf = 100000000
graph = [[Inf] * n for _ in range(n)]

# 최소 값으로 바구기
for i in range(m):
    a, b, c = map(int, input().split())
    if graph[a - 1][b - 1] > c:
        graph[a - 1][b - 1] = c

for k in range(n):
    for i in range(n):
        for j in range(n):
            # 자기 자신으로 오는 경우
            if j == i:
                graph[i][j] = 0

            # k를 거쳐서 가는 것, 최소 값으로 변경
            else:
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

# 행렬 출력
for i in range(n):
    for j in range(n):
        if graph[i][j] == 0:
            print(0, end=' ')
        else:
            print(graph[i][j], end=' ')
    print()