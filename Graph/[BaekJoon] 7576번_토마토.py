from collections import deque
m, n = map(int, input().split())

graph = []
queue = deque([])

# 토마토
for i in range(n):
    graph.append(list(map(int, input().split())))

    for j in range(m):
        if graph[i][j] == 1:
            queue.append([i, j])

# 동서남북
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

result = 0

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            queue.append([i, j])

def bfs():
    while queue:
        x, y = queue.popleft()
        # 동서남북
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 범위 벗어남
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 0:
                queue.append((nx, ny))
                graph[nx][ny] = graph[x][y] + 1

bfs()

for i in graph:
    for node in i:
        # 안익은 토마토 있으면 -1 출력
        if node == 0:
            print(-1)
            exit(0)
    # 다익으면 최댓값 출력
    result = max(result, max(i))

print(result - 1)