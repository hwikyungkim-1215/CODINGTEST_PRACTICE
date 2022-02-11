# 너비 우선 탐색, deque
# BFS는 재귀로 돌아가지 않음(큐를 이용하여 반복 구현만 가능)
from collections import deque

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

graph = {
    1: [2,3,4],
    2: [5],
    3: [5],
    4: [],
    5: [6,7],
    6: [],
    7: [3],
}

print(bfs_iteration(graph,1))