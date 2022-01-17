import sys

input = sys.stdin.readline
n, m = map(int, input().split())
powers = []
names = []

# 이분 탐색
def binary_search(number):
    start = 0
    end = len(powers) - 1

    while start <= end:
        mid = (start + end) // 2
        if number > powers[mid]:
            start = mid + 1
        else:
            end = mid - 1
    print(end)
    print(names[end+1])

# 조건
for i in range(n):
    name, power = input().split()
    power = int(power)
    names.append(name)
    powers.append(power)

# 비교
for i in range(m):
    number = int(input())
    # 이분탐색
    binary_search(number)