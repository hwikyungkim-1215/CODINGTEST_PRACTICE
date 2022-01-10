n = int(input())
a = []

for _ in range(n):
  start, end = map(int, input().split())
  a.append([start, end])

a = sorted(a, key=lambda a: a[0]) # 시작 시간 오름차순
a = sorted(a, key=lambda a: a[1]) # 끝나는 시간 오름차순

last = 0 # 회의 마지막 시간
conut = 0 # 회의 개수

for i, j in a:
  if i >= last:
    conut += 1
    last = j

print(conut)