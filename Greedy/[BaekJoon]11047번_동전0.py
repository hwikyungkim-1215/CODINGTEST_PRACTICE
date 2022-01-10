n,k = map(int, input().split())
a = []
num = 0

for _ in range(n): #동전 단위 넣기
    a.append(int(input()))

a.reverse() #가격 순서뒤집기(내림차순으로 만들기)

for i in range(n):
    if k == 0:
        break
    if a[i]>k:
        continue
    num += k//a[i] #몫 더해주기
    k %= a[i] #나머지 값
print(num)