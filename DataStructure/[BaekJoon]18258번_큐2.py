import sys
from collections import deque

N = int(sys.stdin.readline())

q = deque([])

def push(x):
    q.append(x)

# 큐에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다.
# 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
def pop():
    if (not q):
        return -1
    else:
        return q.popleft()


# 큐에 들어있는 정수의 개수를 출력한다.
def size():
    return len(q)


# 큐가 비어있으면 1, 아니면 0을 출력한다.
def empty():
    if (not q):
        return 1
    else:
        return 0


# 큐의 가장 앞에 있는 정수를 출력한다.
# 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
def front():
    if (not q):
        return -1
    else:
        return q[0]

def back():
    if (not q):
        return -1
    else:
        return q[-1]


for _ in range(N):
    # input()으로 입력받으면 시간초과
    input = sys.stdin.readline().split()
    order = input[0] #명령어 받기

    #명령어에 따라 역할 수행하기

    if order == "push":
        push(input[1])
    elif order == "pop":
        print(pop())
    elif order == "size":
        print(size())
    elif order == "empty":
        print(empty())
    elif order == "front":
        print(front())
    elif order == "back":
        print(back())