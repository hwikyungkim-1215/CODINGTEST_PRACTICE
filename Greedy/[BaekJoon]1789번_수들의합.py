S = int(input())

a = 0
sum = 0
N = 0

for i in range(S):
    N = i+1
    sum += N
    if sum > S:
        N -= 1
        break
    else:
        N
print(N)