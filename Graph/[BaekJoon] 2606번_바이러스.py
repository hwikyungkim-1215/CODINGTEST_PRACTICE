import sys
input = sys.stdin.readline

n = int(input()) # 점 개수
num = int(input()) # 연결 경우 개수
arr = []

# 인접 리스트
graph = [[]*n for _ in range(n+1)]
# graph = defaultdict(list) 와 같음
for _ in range(num):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

# dfs 그대로
def dfs_recursive(graph, start, visited=[]):
    visited.append(start) # 방문한 노드 추가
    for node in graph[start]:
        if node not in visited: # 끝까지 갔을 때(깊이)
            dfs_recursive(graph, node, visited) # 깊이 탐색

    return visited

print(len(dfs_recursive(graph,1))-1)