N, M= map(int, input().split())
number = list(map(int, input().split()))
result = 0

#min = number[0] + number[1] + number[2]
for i in range(N):
   for j in range(i+1, N):
       for k in range(j+1, N):
           if number[i] + number[j] + number[k] > M:
               continue
           else:
               result = max(result, number[i]+number[j]+number[k])
print(result)