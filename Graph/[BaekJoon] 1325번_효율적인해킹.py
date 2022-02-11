import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int,input().split())

result = []

# 인접 리스트
graph = [[]*n for _ in range(n+1)]

# 그래프 생성
for _ in range(m):
    a,b = map(int, input().split())
    graph[b].append(a)

# BFS
def bfs_iteration(graph, root):
    visited = [0]*(n+1)  # 방문한 노드
    queue = deque([root])  # bfs는 queue 사용
    count = 1
    visited[root] = 1

    while (queue):  # queue에 남은 것이 없을 때까지
        node = queue.pop()  # 현재 방문하는 노드

        # node를 방문한 적 없다 -> visited에 추가
        # 해당 노드의 자식 노드들을 queue에 추가
        if node not in visited:
            visited[node] = 1
            visited.append(node)
            queue.extendleft(graph[node])
            count += 1

    return count

# count 담기
result = []
for i in range(1, n+1):
    result.append(bfs_iteration(graph, i))

# 최대값 찾기
max = max(result)
print(max)
for i in range(len(result)):
    if max == result[i]:
        # 컴퓨터 번호 출력(1~N)
        print(i+1, end=' ')
