# 중복 불가
n, m = map(int, input().split())
visited = [False] * (n+1)  # 방문 체크
result = [0] * (m+1)  # 출력

def solve(depth):
    if depth == m+1:  # 탈출 조건
        for i in range(1, m+1):
            print(result[i], end=' ')
        print()
    else:
        for i in range(1, n+1):
            if not visited[i]:  # 방문 안했으면(False)
                visited[i] = True  # 방문 체크(중복 제거)
                result[depth] = i  # 방문한 번호 입력
                #print("result1:", result)
                solve(depth+1)  # 깊이 우선 탐색
                #print("v1:",visited)
                visited[i] = False  # 깊이 방문 완료
                result[depth] = 0 # 방문 내용 제거
                #print("result2:", result)
                #print("v2:", visited)
                #print("=======================")

solve(1)