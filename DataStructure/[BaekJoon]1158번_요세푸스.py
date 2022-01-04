n,k = map(int, input().split())
arr = [] #처음 원에 앉아있는 사람들
answer = [] #제거된 사람들

for i in range(n):
    arr.append(i+1)

num = 0 #제거할 사람 인덱스 번호

while len(arr)>0:
    num = (num+(k-1)) % len(arr)
    popElement = arr.pop(num)
    answer.append(str(popElement))

print("<%s>" %(", ".join(answer)))
