n = int(input())
sum = 0
for _ in range(n):
    a = input()
    s = list(a)
    for j in s:
        if j == "(":
            sum += 1
        elif j == ")":
            sum -= 1
        if sum < 0:
            print("NO")
            break
 
    if sum > 0:
        print("NO")
    elif sum == 0:
        print("YES")
