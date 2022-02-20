# 분할 정복
# 개수, 행, 열
n, r, c = map(int,input().split())

n, r, c = map(int, input().split())
num = -1


def recursive(x, y, N):
    global num

    # 1 X 1
    if N == 2:
        # (x, y) = (0, 0) 에서부터 시작
        for i in range(x, x + N):
            for j in range(y, y + N):
                # 이동 횟수 증가
                num += 1
                # 원하는 행, 열에 도착
                if i == r and j == c:
                    print(num)
                    exit(0)
        return

    # 1사분면에 없으면 건너뛰기(찾는 곳이 3사분면에 있으면, 1,2사분면 건너뛰기)
    if not (x <= r < x + N and y <= c < y + N):
        num += N * N
        return
    # 재귀
    for i in range(x, x + N, N // 2):
        for j in range(y, y + N, N // 2):
            recursive(i, j, N // 2)


recursive(0, 0, 2 ** n)
