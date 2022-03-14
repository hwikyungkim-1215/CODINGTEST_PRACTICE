# 리스트로 입력받기
li = list(map(int, input()))

# 내림차순
li.sort(reverse=True)

# 출력
for i in li:
    print(i, end='')