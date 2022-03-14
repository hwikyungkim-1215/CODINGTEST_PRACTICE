import sys
input = sys.stdin.readline

t = int(input())
li = []
li2 = []

for i in range(t):
    li = list(map(str, input()))
    print(li)
    n = int(input())
    for _ in range(n):
        li2 = input()
    print(li2)


# 뒤집기
def R(s):
    result = []
    n = len(s)
    for i in range(n):
        result.append(s[n-1-i])

    return result









