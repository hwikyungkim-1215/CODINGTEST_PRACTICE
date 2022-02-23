# DFS_스택, 반복문
# 역순으로 방문
def dfs_iteration(graph, root):
    # visited = 방문한 꼭지점들을 기록한 리스트
    visited = []
    # dfs는 stack, bfs는 queue
    stack = [root]

    while (stack):  # 스택에 남은 것이 없을 때까지 반복
        node = stack.pop()  # node : 현재 방문하고 있는 꼭지점

        # 현재 node가 방문한 적 없다 -> visited에 추가한다.
        # 그리고 해당 node의 자식 node들을 stack에 추가한다.
        if (node not in visited):
            visited.append(node)
            stack.extend(graph[node])
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

print(dfs_iteration(graph,1))
