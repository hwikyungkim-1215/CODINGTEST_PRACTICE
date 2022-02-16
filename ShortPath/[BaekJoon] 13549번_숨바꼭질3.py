from collections import deque
# 범위 조심
INF = 100001
distance = [-1] * INF # 거리 리스트
graph = [False] * INF # 방문 체크

n, k = map(int,input().split())

q = deque()
q.append(n) # 현재 위치
graph[n] = True # 방문 체크
distance[n] = 0 # 거리 저장

while q:
    now = q.popleft() # 현재 노드 꺼내기
    if now == k:
        print(distance[now])
        break

    if 0 <= now * 2 < INF and graph[now*2] == False: # now*2 노드를 방문하지 않았을 때
        next = now*2
        q.append(next) # 넣기
        graph[next] = True # 방문 체크
        distance[next] = distance[now] + 0 # 거리 저장

    if 0 <= now -1 < INF and graph[now-1] == False: # now-1 노드를 방문하지 않았을 때
        next = now -1
        q.append(next) # 넣기
        graph[next] = True # 방문 체크
        distance[next] = distance[now] + 1 # 거리 저장

    if 0 <= now + 1 < INF and graph[now+1] == False: # now+1 노드를 방문하지 않았을 때
        next = now + 1
        q.append(next) # 넣기
        graph[next] = True # 방문 체크
        distance[next] = distance[now] + 1 # 거리 저장



