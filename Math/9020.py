# n이하의 숫자들 중 소수 찾기
def prime_list(n):
    sieve = [True] * n
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:
            for j in range(i + i, n, i):
                sieve[j] = False
    return [i for i in range(2, n) if sieve[i] == True]


# n이하의 소수들 중 합이 n
def sum(n):
    li = prime_list(n)
    # n/2으로 반띵한 후 1 ~ n/2 중에서 큰 값부터 찾기
    idx = max([i for i in range(len(li)) if li[i] <= n / 2])
    # 줄여가면서 검사
    for i in range(idx, -1, -1):
        for j in range(i, len(li)):
            # 합이 n인 두 소수
            if li[i] + li[j] == n:
                return [li[i], li[j]]


for _ in range(int(input())):
    n = int(input())
    print(" ".join(map(str, sum(n))))