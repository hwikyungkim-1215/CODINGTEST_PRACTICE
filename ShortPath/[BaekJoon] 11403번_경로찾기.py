# DFS

n = int(input())
visit = [0 for i in range(n)]
s = []

def dfs(v):
    for i in range(n):
        if visit[i] == 0 and s[v][i] == 1: # 방문하지 않은 곳 & 연결된 곳(1)
            visit[i] = 1 # 방문했다고 표시
            dfs(i) #재귀

# 그래프 입력 받기
for i in range(n):
    s.append(list(map(int, input().split())))

# 행렬 출력
for i in range(n):
    dfs(i)
    for j in range(n):
        if visit[j] == 1: # 방문 한 곳인지 확인
            print(1, end=' ')
        else:
            print(0, end=' ')
    print()
    visit = [0 for i in range(n)]