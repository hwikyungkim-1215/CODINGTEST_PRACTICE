from itertools import  accumulate

# 1
a = [1, 2, 3, 4, 5]
b = list(accumulate(a)) # 누적합

print("a:", a)
print("b:", b)

# 2
monthly_income = [1161, 1814, 1270, 2256, 1413, 1842, 2221, 2207, 2450, 2823, 2540, 2134]
result = list(accumulate(monthly_income, max)) #

print(result)