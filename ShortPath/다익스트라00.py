# 다익스트라 가장 기본적인 구현(시간 오래걸림_비효율적)
import sys

input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
start = int(input())

# 주어진 그리프 정보를 담는 N개 길이의 리스트
graph = [[] for _ in range(n+1)]

# 방문 처리 리스트
visited = [[False] * (n+1)]

# 최단 거리 테이블
distance = [INF] * (n+1)

# 그래프 입력
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append(b, c)

# 방문하지 않은 노드이면서 시작노드와 최단거리인 노드 반환
def get_smallest_node():
    min_value = INF # 디폴트 값
    index = 0
    for i in range(1, n+1): # n개 노드
        if not visited[i] and distance[i] < min_value: # 방문하지 않았고, 거리가 무한보다 작은 경우
            min_value = distance[i] # 작은 값으로 업뎃(인덱스 = 0 인 상태)
            index = i # 인덱스 증가 (인덱스 0부터~)
    return index



# 다익스트라 알고리즘
def dijkstra(start):
    # 시작노드 -> 시작노드 거리 계산 및 방문처리
    distance[start] = 0
    visited[start] = True
    # 시작노드의 인접한 노드들에 대해 최단거리 계산
    for i in graph[start]: # graph[0] = (b, c) 꼴
        distance[i[0]] = i[1] # distance[도착노드] = 거리값

    # 시작 노드 제외한 n-1개의 다른 노드들 처리
    for _ in range(n-1):
        now = get_smallest_node() # 방문하지 않은 노드이면서 시작노드와 최단 거리 노드 반환
        visited[now] = True # 방문 처리

        # 해당 노드의 인접한 노드들 간의 거리 계산
        for next in graph[now]:
            cost = distance[now] + next[1] # (시작 -> now거리) + (now -> now의 인접노드 거리)
            if cost < distance[next[0]]: # cost < 시작에서 now의 인접노드 다이렉트 거리
                distance[next[0]] = cost # 작은 값으로 업뎃

# 다익스트라
dijkstra(start)

# 출력
for i in range(1, n+1): # n개
    if distance[i] == INF: # 거리가 무한대 (업뎃이 안 된 경우)
        print('도달 할 수 없음')
    else:
        print(distance[i]) # 최단거리 출력