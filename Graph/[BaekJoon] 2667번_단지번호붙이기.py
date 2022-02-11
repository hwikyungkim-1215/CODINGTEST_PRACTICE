def dfs(x, y):
    global count
    if x <= -1 or x >= n or y <= -1 or y >= n:  # 주어진 범위를 벗어나는 경우
        return False

    if graph[x][y] == 1:  # 현재 노드를 아직 방문하지 않은 경우
        graph[x][y] = 0  # 방문 처리
        count += 1
        # 동서남북 위치들 모두 재귀적으로 호출
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False

n = int(input()) # 정사각형
num = 0
graph = []

for i in range(n):
    graph.append(list(map(int, input())))

# 단지
num = []
# 각 단지별 수
count = 0
for i in range(n):
    for j in range(n):
        if dfs(i, j) == True:
            # 각 단지마다 count 추가
            num.append(count)
            count = 0

# 단지 개수
print(len(num))
# 오름차순 정렬
num.sort()
for i in range(len(num)):
    print(num[i])