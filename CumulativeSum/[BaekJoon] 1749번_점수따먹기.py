import sys
input= sys.stdin.readline

n, m = map(int, input().split())

# 행렬 입력받기
array = [list(map(int,input().split())) for _ in range(n)]

# 누적합 행렬 초기화
sum = [[0] * (m + 1) for _ in range(n + 1)]

#sum[1][1] = array[0][0]

# 누적합 저장
for i in range(1, n+1):
    for j in range(1, m+1):
        sum[i][j] = sum[i-1][j] + sum[i][j-1] - sum[i-1][j-1] + array[i-1][j-1]

result = -400000001

# 최대 누적합 찾기(부분 행렬 구하기)/ 범위 주의!!
for I in range(1, n+1):
    for J in range(1, m+1):
        for i in range(I, n+1):
            for j in range(J, m+1):
                result = max(result, sum[i][j] - sum[i][J-1] - sum[I-1][j] + sum[I-1][J-1])

print(result)


