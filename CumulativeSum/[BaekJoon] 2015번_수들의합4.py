import sys
from collections import defaultdict

input = sys.stdin.readline
# 개수, 합
n, k = map(int, input().split())

nums = list(map(int, input().split()))

count = 0
# 초기값 세팅/ 인덱스 오
cum = defaultdict(int)

for i in range(1, len(nums)):
    nums[i] += nums[i-1]

for i in range(len(nums)):
    if nums[i] == k: # 누적합이 k인 경우 카운트
        count += 1
    count += cum[nums[i]-k]
    cum[nums[i]] += 1 # 누적합이 nums[i]가 되는 경우

print(count)