import sys
from collections import deque

n = int(input())

words = list()

for _ in range(n):
    words.append(sys.stdin.readline().rstrip())


for i in range(n):
    deque = deque(words[i])
    word = "".join(deque)

    print(word)
    #같은 단어
    if word == words[i]:
        break

    if word in words:
        idx = words.index(word)
        print(idx)

        print(words.pop(idx))

        print(words.insert(idx, words[i]))

words = set(words)
print(len(words))

