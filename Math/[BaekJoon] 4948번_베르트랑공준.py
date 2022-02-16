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

while True:
    count = 0
    result = []
    n = int(input())

    if n == 0:
        break

    # 2* n 까지 소수만 구하기
    li = prime_list(2 * n+ 1)
    for i in li:
        if i > n:
            result.append(i)

    print(len(result))
