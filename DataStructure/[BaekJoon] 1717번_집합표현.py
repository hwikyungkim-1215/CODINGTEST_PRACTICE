import sys
input = sys.stdin.readline

n, m = map(int, input().split())

# 부모 테이블 초기화
parent = [i for i in range(n + 1)]

# 부모가 같으면 같은 집합
def find(target):
    if target == parent[target]:
        return target

    parent[target] = find(parent[target])
    return parent[target]

# 합집합
def union(a, b):
    a = find(a)
    b = find(b)

    if not a == b:
        parent[b] = a

for i in range(m):
    x, a, b = map(int, input().split())
    if x == 0:
        union(a, b)
    else:
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")

