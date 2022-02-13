import sys
import heapq
input = sys.stdin.readline
n, m, k, x = map(int, input().split())
INF = int(1e9)

# 그래프 생성
distance = [INF] * (n+1)
graph = [[] for _ in range(n+1)]

# 그래프 입력
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append((b,1))


# 다익스트라 알고리즘
def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))  # 시작노드 정보 우선순위 큐에 삽입
    distance[start] = 0            # 시작노드 -> 시작노드 거리 기록

    while q:
        dist, node = heapq.heappop(q)

        # 큐에서 뽑아낸 거리가 이미 갱신된 거리보다 클 경우(=방문한 셈) 무시
        if distance[node] < dist:
            continue

        # 큐에서 뽑아낸 노드와 연결된 인접노드들 탐색
        for next in graph[node]:
            cost = distance[node] + next[1]   # 시작 -> node거리 + node -> node의 인접노드 거리
            if cost < distance[next[0]]:      # cost < 시작 -> node의 인접노드 거리
                distance[next[0]] = cost # 작은 걸로 업뎃
                heapq.heappush(q, (cost, next[0]))

# 다익스트라
dijkstra(x)

result = []
# 결과 값 넣기
for i in range(1, n+1):
    if distance[i] == k:
        result.append(i)

# 출력
if len(result) != 0:
    for i in result:
        print(i, end='\n')
else:
    print(-1)