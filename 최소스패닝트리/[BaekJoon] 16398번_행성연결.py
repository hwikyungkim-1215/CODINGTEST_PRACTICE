# 최소신장트리 문제
# 크루스칼 알고리즘
import sys
input = sys.stdin.readline

# find 연산
def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

# union 연산
def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n = int(input())
edges = []
# 부모 테이블 초기화
parent = [i for i in range(n)]

# 행렬 입력받기
graph = [list(map(int, input().split())) for _ in range(n)]

# 간선 정보(대칭 행렬로 주어짐-> 상삼각행렬만 저장하면 됨)
for a in range(n):
    for b in range(a+1, n):
        edges.append((graph[a][b], a, b))

# 간선 정보 비용 기준으로 오름차순 정렬
edges.sort()

# 최소 신장 트리 계산 변수 정의
total_cost = 0



for edge in edges:
    cost, a, b = edge

    if find_parent(a) != find_parent(b):
        union_parent(a, b)
        total_cost += cost

print(total_cost)