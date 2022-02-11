n, m = map(int, input().split())
l1, l2 = set(), set()

for _ in range(n):
    l1.add(input())
    #print("l1:",l1)

for _ in range(m):
    l2.add(input())
    #print("l2:", l2)

li = sorted(l1 & l2) #합집합

#print(li)
print(len(li))
for i in li:
    print(i)




