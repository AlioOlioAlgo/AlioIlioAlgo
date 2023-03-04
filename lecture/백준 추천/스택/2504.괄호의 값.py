"""
 *packageName    : 
 * fileName       : 2504.괄호의 값
 * author         : ipeac
 * date           : 2023-03-04
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2023-03-04        ipeac       최초 생성
 """
import sys

input = sys.stdin.readline

arr = input().rstrip()
stack = []
for value in arr:
    if value == '(' or value == '[':
        stack.append(value)
    elif value == ')':
        temp = 0
        while stack:
            top = stack.pop()
            if top == '(':
                temp = 2 if temp == 0 else temp * 2
                stack.append(temp)
                break
            elif isinstance(top, int):
                temp += top
            else:
                print(0)
                sys.exit(0)
        else:
            print(0)
            sys.exit(0)

    elif value == ']':
        temp = 0
        while stack:
            top = stack.pop()
            if top == '[':
                temp = 3 if temp == 0 else temp * 3
                stack.append(temp)
                break
            elif isinstance(top, int):
                temp += top
            else:  # break 된 경우가 아니면 오류임
                print(0)
                sys.exit(0)
        else:
            print(0)
            sys.exit(0)

    else:
        print(0)
        sys.exit(0)
print(sum(stack) if all(isinstance(i, int) for i in stack) else 0)
