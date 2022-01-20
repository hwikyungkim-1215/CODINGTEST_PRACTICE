arr = int(input())

for _ in range(arr):
    n, m = map(int, input().split())
    li = list(map(int, input().split()))
    index = [0 for i in range(n)]
    index[m] = 'target'
    count = 0

    # 가장 큰 값 찾기
    while True:
        # 가장 큰 값이 맨 앞으로
        if li[0] == max(li):
            count += 1
            # 찾는 값이면
            if index[0] == 'target':
                print(count)
                break
            else:
                del li[0]
                del index[0]
        else:
            li.append(li.pop(0))
            index.append(index.pop(0))



