n = int(input())
graph = []

for i in range(n):
    graph.append(list(map(int, input().split())))

def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= n:
        return False

    if graph[x][y] == 1:
        graph[x][y] = 0
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False

blue = 0
white = 0

for i in range(n // 2):
    if white == 0:
        break
    for j in [n//2, n]:
        if dfs(i, j) == True:
            blue += 1
        else:
            white += 1

for i in range(n // 2, n):
    if white == 0:
        print(0)
        print(1)
        break
    for j in [n // 2, n]:
        if dfs(i, j) == True:
            blue += 1
        else:
            white += 1
        print(white)
        print(blue)









