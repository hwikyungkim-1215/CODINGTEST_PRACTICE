n = int(input()) #문제의 수
color = list(input()) #문제를 어떤 색으로 칠할지
countR = 0
countB = 0
result = 1

color.append('x') #범위 벗어나는 오류 해결

for i in range(n+1):
    if color[i] == 'R':
        countR += 1
        if color[i+1] == 'R': #연속
            countR -= 1
    elif color[i] == 'B':
        countB += 1
        if color[i+1] == 'B': #연속
            countB -= 1

if countR > countB:
    result += countB
else:
    result += countR

print(result)
