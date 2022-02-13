import sys
input = sys.stdin.readline

# 지역 수, 수색범위, 길의 개수
n, m, r = map(int, input().split())

# 각 구역의 아이템 수
item = list(map(int, input().split()))

# 그래프 입력
INF = int(1e9)
graph = [[INF] * (n+1) for _ in range(n+1)]

for _ in range(r):
    # start, end, 길이
    a, b, l = map(int, input().split())
    # 양방향
    graph[a][b] = l
    graph[b][a] = l


for i in range(n + 1):
      for j in range(n + 1):
            # 자기 자신
            if i == j:
                  graph[i][j] = 0

# 플로이드 와샬
for k in range(1, n + 1):
      for i in range(1, n + 1):
            for j in range(1, n + 1):
                  # min(k를 지나서 가기, 바로 가기)
                  graph[i][j] = min(graph[i][k] + graph[k][j], graph[i][j])


# 결과
result = 0
for g in graph:
    ans = 0
    for i in range(1, n + 1):
        if g[i] <= m: # 제한 거리
                ans += item[i - 1]
    # 이전 시작 점들과 비교**
    result = max(result, ans)

print(result)

