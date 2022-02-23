# DFS_재귀
def dfs_recursive(graph, start, visited=[]):
    visited.append(start) # 방문한 노드 추가

    for node in graph[start]:
        if node not in visited: # 끝까지 갔을 때(깊이)
            dfs_recursive(graph, node, visited) # 깊이 탐색

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

print(dfs_recursive(graph,1))