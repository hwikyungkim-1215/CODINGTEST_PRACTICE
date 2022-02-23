from collections import deque

#stack
stack = []
stack.append(1) # 오른쪽에 삽입
stack.append(2)
stack.append(3)
stack.append(4)
print(stack)

stack.pop() # 오른쪽에서 삭제
stack.pop()
print(stack)


# queue
queue = deque()
queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)
print(queue)

queue.popleft()
queue.popleft()
print(queue) # 먼저 들어온 순서대로 출력

queue.reverse() # 역순으로 바꾸기
print(queue) # 나중에 들어온 원소부터 출력