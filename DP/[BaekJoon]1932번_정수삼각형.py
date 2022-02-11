n = int(input()) # 삼각형 크기
a = [] # 7 3 8 8 1 0 ...

for i in range(n):
    a.append(list(map(int, input().split())))

for i in range(1, n): # 줄 개수(행) (ex. 1부터 5까지) / 하각행렬 꼴
    for j in range(i+1): # 한 줄에 있는 수의 개수(열) (ex. 1 -> 2 -> ... -> 5)
        if j == 0: # 맨 왼쪽인 경우 위에 숫자 더하기
            a[i][j] += + a[i - 1][j]
        elif i == j: # 맨 오른쪽인 경우 왼쪽 위에 숫자 더하기
            a[i][j] += + a[i - 1][j - 1]
        else: # 맨 왼/오른 쪽이 아닌 경우 왼쪽 위 or 오른 쪽 위 중에 큰거 더하기
            a[i][j] +=  max(a[i - 1][j - 1], a[i - 1][j])

print(max(a[n - 1]))