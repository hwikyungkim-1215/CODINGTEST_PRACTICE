from itertools import combinations
arr = list(input())

# 괄호 (
index = []
# 괄호 짝짓기
index2 = []

# 비어있는 집합
result = set()

for i, j in enumerate(list(arr)):
    if arr[i] == "(":
        index.append(i)
    elif arr[i] == ")":
        start = index.pop()
        end = i
        index2.append([start,end])

for i in range(1,len(index2)+1):
    com = combinations(index2,i)
    for j in com:
        # 입력받은 arr, 리스트로 [[3, 5], [0, 6]]
        tmp = list(arr)
        # com(조합)의 경우의 수에 따라 괄호() 없애기
        for k in j:
            start,end = k
            # 3, 0
            tmp[start] = ''
            # 5, 6
            tmp[end] = ''
        result.add(''.join(tmp))

for i in sorted(list(result)):
    print(i)