n = int(input()) #도시 수 입력받기
d = list(map(int,input().split())) #도로 길이 입력받기
cost = list(map(int,input().split())) #리터 당 비용

sum = 0 #총 비용
m = cost[0]

for i in range(n-1):
    if cost[i] < m:
        m = cost[i]
    sum += m * d[i]

print(sum)
    
