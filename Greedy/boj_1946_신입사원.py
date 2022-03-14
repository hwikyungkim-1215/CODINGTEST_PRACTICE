import sys
input = sys.stdin.readline
t = int(input())

for _ in range(t):
    count = 1
    people = []
    # 지원자 수
    n = int(input())
    for _ in range(n):
        a, b = (map(int, input().split()))
        people.append([a, b])
    # 서류기준(앞에꺼 기준) 오름차순 정렬
    people.sort()
    #print("people:", people)

    # 서류 1등의 면접 등수(기준 점) -> 서류 1등은 무조건 합격
    max = people[0][1]

    # 서류 2등부터 갱신
    for i in range(1, n):
        if max > people[i][1]:
            count += 1 # 합격자 수 갱신
            # max 값(면접 순위) 갱신
            max = people[i][1]
    print(count)


