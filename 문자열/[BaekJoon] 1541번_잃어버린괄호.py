# 마이너스로 구분하여 입력받기
n = input().split('-')
li = []
total = []

for i in n:
    # 매번 초기화
    sum = 0
    # 더하기로 분리
    li2 = i.split('+')
    #print(li2)
    # 더하기 값 계산
    for j in li2:
        sum += int(j)
    total.append(sum)

result = total[0]
for i in range(1, len(total)):
    result -= total[i]

print(result)



