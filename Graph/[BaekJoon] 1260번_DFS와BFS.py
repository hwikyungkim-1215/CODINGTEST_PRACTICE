import sys
from collections import deque

input = sys.stdin.readline

n, m, v = map(int,input().split())

# 인접 리스트
graph = [[]*n for _ in range(n+1)]
for _ in range(m): # 간선의 개수 만큼 반복
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    # 정렬 안하면 실
    graph[a].sort()
    graph[b].sort()

# DFS
def dfs_recursive(graph, start, visited=[]):
    visited.append(start) # 방문한 노드 추가

    for node in graph[start]:
        if node not in visited: # 끝까지 갔을 때(깊이)
            dfs_recursive(graph, node, visited) # 깊이 탐색

    return visited

# BFS
def bfs_iteration(graph, root):
    visited = []  # 방문한 노드
    queue = deque([root])  # bfs는 queue 사용

    while (queue):  # queue에 남은 것이 없을 때까지
        node = queue.pop()  # 현재 방문하는 노드

        # node를 방문한 적 없다 -> visited에 추가
        # 해당 노드의 자식 노드들을 queue에 추가
        if node not in visited:
            visited.append(node)
            queue.extendleft(graph[node])

    return visited

# 띄어쓰기 형태로 출력
def result(fun):
    for i in range(len(fun)):
        print(fun[i], end = ' ')

result(dfs_recursive(graph,v))
print()
result(bfs_iteration(graph,v))
