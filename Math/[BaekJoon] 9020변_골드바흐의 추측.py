from itertools import combinations, product


# 소수 찾는 알고리즘(에라토스테네스의 체)
def prime_list(n):
    # 에라토스테네스의 체 초기화: n개 요소에 True 설정(소수로 간주)
    sieve = [True] * n

    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:           # i가 소수인 경우
            for j in range(i+i, n, i): # i이후 i의 배수들을 False 판정
                sieve[j] = False

    # 소수 목록 산출
    return [i for i in range(2, n) if sieve[i] == True]

result = []
c = []
a = []
b = []
result = 0
j1 = 0

# 두 소수의 합 = n
def sum(n):
    li = prime_list(n) # 소수
    com = [i for i in combinations(li,2)]

    for i in range(len(li)):
        A = li[i]
        com.append((A,A))


    for i in range(len(com)):
        if (com[i][0] + com[i][1]) == n:
            a.append(com[i][0])
            b.append(com[i][1])

    for j in range(len(a)):
        c.append(b[j] - a[j])
        result = min(c)

    for j in range(len(a)):
        if result == c[j]:
            j1 = j
            #print("j1", j1)
    return [a[j1], b[j1]]

for _ in range(int(input())):
    n = int(input())
    print(" ".join(map(str,sum(n))))

