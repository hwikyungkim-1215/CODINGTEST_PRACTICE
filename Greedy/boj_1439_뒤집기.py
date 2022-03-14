s = input()
change = []

for i in range(1, len(s)):
    # 이전 값과 현재 값의 비교(0->1, 1->0 처럼 변화하면 append)
    if s[i - 1] != s[i]:
        change.append(i)

isOdd = False

# 홀수면
if len(change) % 2 == 1:
    isOdd = True

# 짝수인 경우(2로 나누기)
result = len(change) // 2

# 홀수일 경우(2로 나눈 후 + 1)
if isOdd:
    result += 1
print(result)