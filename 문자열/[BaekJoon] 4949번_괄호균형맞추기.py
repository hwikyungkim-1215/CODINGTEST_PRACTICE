while True:
    s = input()
    li = []
    if s == ".":
        break
    for i in s:
        # 괄호 시작 -> 리스트에 다 넣기
        if i == '(' or i == '[':
            li.append(i)
        # 종료 괄호1
        elif i == ')':
            # 괄호 시작이 존재하고, 짝이 맞을 경우
            if len(li) != 0 and li[-1] == '(':
                li.pop()
            # 괄호 시작이 존재하지 않거나, 짝이 안맞을 경우
            else:
                li.append(i)
                break

        # 종료 괄호2
        elif i == ']':
            if len(li) != 0 and li[-1] == '[':
                li.pop()
            else:
                li.append(i)
                break

    if len(li) == 0:
        print("yes")
    else:
        print("no")

