# 중복 가능
n, m = map(int, input().split())
# 리스트 입력
li = sorted(set(list(map(int, input().split()))))

result = [0] * (m)
#print(li)

def solve(depth):
    if depth == m:  # 탈출 조건
        for i in range(m):
            print(result[i], end=' ')
        print()
        return
    for i in range(len(li)):
        result[depth] = li[i]  # 방문한 번호 입력
        solve(depth+1)  # 깊이 우선 탐색
        result[depth] = 0  # 방문 내용 제거

solve(0)