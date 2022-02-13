import sys
import heapq
input = sys.stdin.readline

# 정점 수, 간선 수
v, e = map(int, input().split())

# 정점 번호
start = int(input())

# 그래프 생성
INF = int(1e9)
distance = [INF] * (v+1)
graph = [[] for _ in range(v+1)]

# 그래프 입력
for _ in range(e):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

# 다익스트라 알고리즘
def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, node = heapq.heappop(q)

        # 이미 방문했으면 무시
        if distance[node] < dist:
            continue

        # 큐에서 뽑아낸 노드와 연결된 인접노드들 탐색
        for next in graph[node]:
            cost = distance[node] + next[1]
            if cost < distance[next[0]]:
                distance[next[0]] = cost # 작은 걸로 업뎃
                heapq.heappush(q, (cost, next[0]))

# 다익스트라
dijkstra(start)

# 출력
for i in range(1, len(distance)):
    if distance[i] == INF:
        print('INF')
    else:
        print(distance[i])