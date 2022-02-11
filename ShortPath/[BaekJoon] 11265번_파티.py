n, m = map(int, input().split())

graph = []

# 입력
for i in range(n):
    graph.append(list(map(int, input().split())))

# 플로이드 워셜 알고리즘
for k in range(n):
    for i in range(n):
        for j in range(n):
            if graph[i][j] > (graph[i][k] + graph[k][j]):
                graph[i][j] = graph[i][k] + graph[k][j] # 작은 값으로 대체

# m번 입력
for _ in range(m):
    # 시작, 끝, 시간
    a, b, c = map(int, input().split())
    # 시작 위치 1부터니까
    if c >= graph[a-1][b-1]:
        print("Enjoy other party")
    else:
        print("Stay here")

