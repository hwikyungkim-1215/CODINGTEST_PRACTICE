N, M = map(int, input().split())
visited = [False] * N  # 방문 체크
result = []  # 출력

def solve(depth, N, M):
    if depth == M:  # 탈출 조건
        print(' '.join(map(str, result)))
        return
    for i in range(len(visited)):  # 방문 체크
        if not visited[i]:  # 방문 안했으면
            visited[i] = True  # 방문 시작(중복 제거)
            result.append(i+1)  # 방문한 번호 입력
            solve(depth+1, N, M)  # 깊이 우선 탐색
            visited[i] = False  # 깊이 방문 완료
            result.pop()  # 방문 내용 제거

solve(0, N, M)