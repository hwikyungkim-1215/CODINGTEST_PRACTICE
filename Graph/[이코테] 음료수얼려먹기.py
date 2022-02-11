def dfs(x, y):
    if x <= -1 or x >= N or y <= -1 or y >= M:  # 주어진 범위를 벗어나는 경우
        return False

    if graph[x][y] == 0:  # 현재 노드를 아직 방문하지 않은 경우
        graph[x][y] = 1  # 방문 처리
        # 상, 하, 좌, 우 위치들 모두 재귀적으로 호출
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False


N, M = map(int, input().split())
graph = []

for i in range(N):
    graph.append(list(map(int, input())))

result = 0
for i in range(N):
    for j in range(M):
        if dfs(i, j) == True:
            result += 1
print(result)
