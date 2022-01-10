n = int(input()) #n킬로그램

result = 0
while n >=0:
    if n % 5 == 0: #5의배수
        result += (n//5)
        print(result)
        break
    n -= 3 #5의배수 만들기
    result += 1 #3kg 가방 개수 증가
else:
    print(-1)
