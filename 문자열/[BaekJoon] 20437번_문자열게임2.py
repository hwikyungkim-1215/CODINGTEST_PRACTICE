import sys
from collections import defaultdict

t = int(sys.stdin.readline())

# testCase만큼 반복
for test_num in range(t):
    # 문자, k 입력받기
    string = input()
    K = int(input())

    len_str = len(string)

    # K개 이상 있는 문자만 따로 저장
    alpha = defaultdict(list)

    # alpha = {'u': [1, 7], 'r': [4, 11], 'a': [5, 8, 13], 'o': [10, 15]}
    # u는 인덱스 1, 7인 자리에 존재한다는 의미
    for i in range(len_str):
        if string.count(string[i]) >= K:
            alpha[string[i]].append(i)


    # K개 이상 있는 문자가 없다면 -1
    if not alpha:
        print(-1)
    else:
        min_str = 0
        max_str = 0

        for idx_lst in alpha.values():
            print("idx_lst:", idx_lst)
            # super에서 K=3인 경우는 sup, upe, per 이므로
            # index = 0에서부터 문자의 총 길이에서 k를 빼준 index까지 진행
            for j in range(len(idx_lst) - K + 1):
                # 'u': [1, 7]에서 7 - 1 + 1 = 7(u를 k개 포함한 길이)
                temp = idx_lst[j + K - 1] - idx_lst[j] + 1

                # 문자열 길이 최소값
                if temp < min_str:
                    min_str = temp

                # 문자열 길이 최대값(최댓값으로 갱신)
                if temp > max_str:
                    max_str = temp

        print(min_str, max_str)




