import sys

input = sys.stdin.readline

n = int(input()) #계단의 개수

score = []
sum = []

for _ in range(n): #점수 넣기
    score.append(int(input()))

if n==1:
    print(score[0])
    exit()
elif n == 2:
    print(max(score[0]+score[1], score[1]))
    exit()

sum.append(score[0])
sum.append(max(score[0] + score[1], score[1]))
sum.append(max(score[0] + score[2], score[1] + score[2]))

for i in range(3, n):
    sum.append(max(sum[i-3] + score[i-1] + score[i], sum[i-2] + score[i]))

print(sum[-1])