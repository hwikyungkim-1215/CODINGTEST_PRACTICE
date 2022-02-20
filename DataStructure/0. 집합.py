# 교집합
set1 = set([1,2,3,4,5])
set2 = set([4,5,6,7])

print(set1 & set2)
print(set1.intersection(set2))

# 합집합
print(set1 | set2)
print(set1.union(set2))

# 차집합
print(set1 - set2)
print(set1.difference(set2))

# 대칭차집합(set1 - set2 더하기 set2 - set1)
print(set1 ^ set2)