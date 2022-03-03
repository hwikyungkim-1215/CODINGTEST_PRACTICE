# 중복 불가
n, m = map(int, input().split())
# 리스트 입력
li = list(map(int, input().split()))
li.sort()

visited = [False] * (n+1)  # 방문 체크
result = [0] * (m)

def solve(depth):
    if depth == m:  # 탈출 조건
        for i in range(m):
            print(result[i], end=' ')
        print()
        return
    overlap = 0
    for i in range(len(li)):
        if not visited[i] and overlap != li[i]:  # 방문 안했으면(False)
            visited[i] = True  # 방문 체크(중복 제거)
            result[depth] = li[i]  # 방문한 번호 입력
            overlap = li[i]
            solve(depth+1)  # 깊이 우선 탐색
            visited[i] = False
            result[depth] = 0  # 방문 내용 제거

solve(0)