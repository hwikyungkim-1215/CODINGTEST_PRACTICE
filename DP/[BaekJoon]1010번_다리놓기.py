import math

n = int(input()) #입력 개수

for _ in range(n):
    N,M = map(int, input().split())
    if N==0:
        print(0)
        continue
    # mCn
    result = math.factorial(M) // (math.factorial(N) * math.factorial(M-N))
    print(result)




