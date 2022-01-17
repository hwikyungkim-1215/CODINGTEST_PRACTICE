import sys

C, P = map(int, input().split())
first = list(map(int, sys.stdin.readline().split()))

result = 0

#경우마다 나누기
if P == 1:
    #0 모두 가능
    result += C

    # 0000 모든 층이 같을 때
    for i in range(C - 3):
        if first[i] == first[i + 1] and first[i + 1] == first[i + 2] and first[i + 2] == first[i + 3]:
            result += 1

if P == 2:
    # 00 2칸 연속
    for i in range(C-1):
        if first[i] == first[i + 1]:
            result += 1

if P == 3:
    # 001
    for i in range(C-2):
        if first[i] == first[i + 1] and first[i + 2] == first[i + 1] + 1:
            result += 1
    # 10
    for i in range(C-1):
        if first[i] == first[i + 1] + 1:
            result += 1

if P == 4:
    # 100
    for i in range(C-2):
        if first[i] == first[i + 1] + 1 and first[i + 1] == first[i + 2]:
            result += 1
    # 01
    for i in range(C-1):
        if first[i + 1] == first[i] + 1:
            result += 1

if P == 5:
    # 000
    for i in range(C-2):
        if first[i] == first[i + 1] and first[i + 1] == first[i + 2]:
            result += 1
    # 01
    for i in range(C-1):
        if first[i + 1] == first[i] + 1:
            result += 1

    # 101
    for i in range(C - 2):
        if first[i] == first[i + 1] + 1 and first[i + 2] == first[i + 1] + 1:
            result += 1

    # 10
    for i in range(C - 1):
        if first[i] == first[i + 1] + 1:
            result += 1


if P == 6:
    # 000
    for i in range(C-2):
        if first[i] == first[i+1] and first[i+1] == first[i+2]:
            result += 1

    # 20
    for i in range(C - 1):
        if first[i] == first[i+1]+2:
            result += 1

    # 011
    for i in range(C - 2):
        if first[i] == first[i+1]-1 and first[i+1] == first[i+2]:
            result += 1
    # 00
    for i in range(C-1):
        if first[i] == first[i+1]:
            result += 1
if P == 7:
    # 000
    for i in range(C-2):
        if first[i] == first[i+1] and first[i+1] == first[i+2]:
            result += 1

    # 00
    for i in range(C - 1):
        if first[i] == first[i+1]:
            result += 1

    # 110
    for i in range(C - 2):
        if first[i] == first[i+1] and first[i+1] == first[i+2] + 1:
            result += 1
    # 02
    for i in range(C - 1):
        if first[i + 1] == first[i] + 2:
            result += 1

print(result)