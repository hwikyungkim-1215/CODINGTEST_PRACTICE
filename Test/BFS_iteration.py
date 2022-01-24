def bfs_iteration(graph, root):
    visited = []  ## visited = 방문한 노드들을 기록한 리스트
    queue = deque([root])  ## bfs는 queue개념을 이용한다.

    while (queue):  ## queue에 남은 것이 없을 때까지 반복
        node = queue.pop()  ## node : 현재 방문하고 있는 노드

        ## 현재 node를 방문한 적 없다. -> visited에 추가
        ## visited에 추가 후, 해당 노드의 자식 노드들을 queue에 추가
        if node not in visited:
            visited.append(node)
            queue.extendleft(graph[node])
    return visited