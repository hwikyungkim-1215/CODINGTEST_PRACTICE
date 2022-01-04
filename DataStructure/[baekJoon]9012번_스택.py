import sys

# 정수 X를 스택에 넣는 연산이다.
def push(x):
    stack.append(x)

# 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 
# 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
def pop():
    if(not stack):
        return -1
    else:
        return stack.pop()

# 스택에 들어있는 정수의 개수를 출력한다.
def size():
    return len(stack)

# 스택이 비어있으면 1, 아니면 0을 출력한다.
def empty():
    if(not stack):
        return -1
    else:
        return 0
 
# 스택의 가장 위에 있는 정수를 출력한다. 
# 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
def top():
    if(not stack):
        return -1
    else:
        return stack[-1] 

N = int(sys.stdin.readline().rstrip())
stack = []

for _ in range(N):
    input = sys.stdin.readline().rstrip().split() #input()으로 입력받으면 시간초과

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
    elif order == "top":
        print(top())
