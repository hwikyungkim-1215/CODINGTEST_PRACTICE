# 네트워크 딜레이 타임
import collections
import heapq

N = int(input())
K = int(input())

for _ in range(N-1):

def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
    # 존재 유뮤 판단 안해도 ok
    graph = collections.defaultdict(list) # 예외처리
    # 그래프 인접 리스트 구성
    for u, v, w in times: # 출발, 도착, 시간
        graph[u].append((u, v))

    # 큐 변수: [(소요시간, 정점)]
    Q = [(0, K)] # 시작점이 k이므로
    # 거리 dist 초기값
    dist = collections.defaultdict(int)

    # 우선순위 큐 최솟값 기준으로 정점까지 최단경로 삽입
    while Q:
        time, node = heapq.heappop(Q)
        if node not in dist:
            dist[node] = time
            for v, w in graph[node]:
                heapq.heappop(Q, (alt, v))

    # 모든 노드의 최단 경로 존재 여부 판별
    if len(dist) == N:
        return max(dist.values())
    return -1
