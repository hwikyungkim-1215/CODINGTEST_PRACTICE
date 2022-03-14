
# 가장 많은 알파벳에 가장 큰 수 매칭하기 -> 그리디
# 1. 알파벳과 자리수 매칭하기
# 2. 숫자만 리스트에 저장하기 -> 내림차순 정렬하기
# 3. 9부터 -1하며 매칭
import sys
input = sys.stdin.readline
n = int(input())

alpha = []
alphabet = [0] * 26
alpha_dict = {} # 단어 내의 알파벳별로 수를 저장할 딕셔너리
numList = [] # 수를 저장할 리스트

# 단어 입력받기
for _ in range(n):
    alpha.append(input().rstrip())

# ['GCF', 'ACDEB']
#print(alpha)

#print("dic:", alpha_dict)

for i in range(n): # 모든 단어에 대해서
    for j in range(len(alpha[i])): # 각 단어의 길이만큼 실행
        if alpha[i][j] in alpha_dict: # 단어의 알파벳이 이미 dict에 있으면 -> ACA일때 A: 100 + 1
            alpha_dict[alpha[i][j]] += 10 ** (len(alpha[i])-j-1) # 자리에 맞게 추가 ( 1의 자리면 1 )
        else:   # 자리에 없으면 새로 추가 ( 10의 자리면 10 )
            alpha_dict[alpha[i][j]] = 10 ** (len(alpha[i])-j-1)

# dic2: {'G': 100, 'C': 1010, 'F': 1, 'A': 10000, 'D': 100, 'E': 10, 'B': 1}
#print("dic2:", alpha_dict)

for val in alpha_dict.values(): # dict에 저장된 수들을 모두 리스트에 추가
    numList.append(val)

#print("numlist:", numList)

numList.sort(reverse=True) # 수들을 내림차순 정렬

sum = 0
pows = 9
for i in numList: # 첫 번째 부터 가장 큰 부분을 차지하므로 9를 곱해준다
    sum += pows * i
    pows -= 1
# 내려갈수록 그 알파벳이 차지하는 비중이 적으므로 -1
print(sum)