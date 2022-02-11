import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
n = int(input())

# 인접 리스트
graph = [[]*n for _ in range(n+1)]

# 그래프 생성
for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited=[0]*(n+1)
# DFS
def dfs_recursive(start):
    for i in graph[start]:
        if visited[i] == 0:
            visited[i] = start # 방문하지 않았으면 현재노드 -> 부모노드에 저장
            dfs_recursive(i) # 깊이 탐색


dfs_recursive(1)

# 부모 노드 출력
for i in range(2,n+1):
    print(visited[i])





