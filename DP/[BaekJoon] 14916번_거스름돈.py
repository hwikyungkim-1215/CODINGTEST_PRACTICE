n = int(input())

result = 0
while n >= 0:
    if n % 5 == 0: #5의 배수이면
        result += (n//5)
        print(result)
        break
    n -= 2
    result += 1 #2원짜리 동전개수 증가
else:
    print(-1)
