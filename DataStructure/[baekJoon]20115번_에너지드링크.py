n = int(input()) #에너지드링크 수
drink = list(map(int,input().split())) #에너지드링크 양
 
drink.sort(reverse=True) #양을 내림차순으로 정렬
sum = drink[0] #가장 많은 양

for i in range(1,n):
    sum += (drink[i]/2)

print('%g' %sum)
