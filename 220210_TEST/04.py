# 오르막 수
n = int(input()) # 수의 길이

result2 = [1]*10

for i in range(1, n):
    for j in range(1, 10):
        result2[j] += result2[j-1]

print(sum(result2) % 10007)






