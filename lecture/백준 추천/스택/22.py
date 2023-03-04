def calculate(s):
    stack = []
    for i in s:
        if i == '(' or i == '[':
            stack.append(i)
        elif i == ')':
            temp = 0
            while stack:
                top = stack.pop()
                if top == '(':
                    stack.append(2 if temp == 0 else temp * 2)
                    break
                elif isinstance(top, int):
                    temp += top
        elif i == ']':
            temp = 0
            while stack:
                top = stack.pop()
                if top == '[':
                    stack.append(3 if temp == 0 else temp * 3)
                    break
                elif isinstance(top, int):
                    temp += top
        else:
            return 0
    return sum(stack) if all(isinstance(i, int) for i in stack) else 0

s = input().rstrip()
print(calculate(s))
