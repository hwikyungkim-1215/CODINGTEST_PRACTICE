arr = list(input())
# 수식
stack=[]
# 문자 ABC
result=''

for i in arr:
    # 알파벳인지 확인
    if i.isalpha():
        result += i
    else:
        if i == '(':
            stack.append(i)
        # 가장 높은 우선순위, result에 모두 추가
        elif i == '*' or i == '/':
            while stack and (stack[-1] == '*' or stack[-1] =='/'):
                result += stack.pop()
            stack.append(i)
        # 가장 낮은 우선순위
        elif i == '+' or i == '-':
            while stack and stack[-1] != '(':
                result+= stack.pop()
            stack.append(i)
        # ( ) 사이에 모든 연산자 result에 추가, ( pop
        elif i == ')':
            while stack and stack[-1] != '(':
                result += stack.pop()
            stack.pop()

# 수식을 문자뒤에 넣기(후위 표기식)
while stack :
    result += stack.pop()

print(result)