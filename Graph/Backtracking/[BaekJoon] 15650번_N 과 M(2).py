N, M = map(int, input().split())
visited = [False] * N # 방문 체크
result, result_all = [], []

def solve(depth, N, M):
    if depth == M:
        out_str = ' '.join(map(str, sorted(result)))
        if out_str not in result_all:
            result_all.append(out_str)
        return
    for i in range(N):
        if not visited[i]:
            visited[i] = True # 방문 체크
            result.append(i+1) # 방문 번호 입력
            solve(depth+1, N, M)
            visited[i] = False # 방문 완료
            result.pop()
solve(0, N, M)

for i in result_all:
    print(i)