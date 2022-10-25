"""
 *packageName    : 
 * fileName       : 박상준
 * author         : ipeac
 * date           : 2022-10-24
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-10-24        ipeac       최초 생성
 """

while True:
    sentence = list(map(str, input()))
    if len(sentence) == 1 and sentence[-1] == '.':
        exit()
    sentence = sentence[:-1]
    pivot = ''
    stack = []
    for idx, sence in enumerate(sentence):
        if sence == '(':
            stack.append('(')
            pivot = '('
        elif sence == ')':
            stack.append(')')
            pivot = ')'
        
        if sence == '[':
            stack.append('[')
            pivot = '['
        elif sence == ']':
            stack.append(']')
            pivot = ']'
        if len(stack) >= 2 and stack[-1] == ']' and stack[-2] == '[':
            stack.pop()
            stack.pop()
        elif len(stack) >= 2 and stack[-1] == ')' and stack[-2] == '(':
            stack.pop()
            stack.pop()
    if not stack:
        print("yes")
    else:
        print('no')
