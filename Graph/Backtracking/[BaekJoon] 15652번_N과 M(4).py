# 비내림차순, 사전 순 출력
n, m = map(int, input().split())
result = [0] * (m+1)

def solve(depth):
    if depth == m+1:  # 탈출 조건
        for i in range(1, m+1):
            print(result[i], end=' ')
        print()
    else:
        for i in range(1,n+1):
            if max(result) <= i: # 비내림차순
                result[depth] = i  # 방문한 번호 입력
                solve(depth+1)  # 깊이 우선 탐색
                result[depth] = 0  # 방문 내용 제거
solve(1)