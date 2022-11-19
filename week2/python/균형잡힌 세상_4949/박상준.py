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
    if len(sentence) == 1 and sentence[-1] == '.':  # 길이가 1이고 마지막이 . 이라면.. 그냥 입력 종료!
        exit()
    sentence = sentence[:-1]  # . 제거
    pivot = ''
    stack = []  # 스택에 해당 괄호를 순차적으로 담음 ㅇㅇ
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
        
        #     여기까지 담는 역할
        if len(stack) >= 2 and stack[-1] == ']' and stack[-2] == '[':  # 스택이 2이상존재하고. || 스택 마지막 두번째 [   마지막 ] 인경우 소거함.
            stack.pop()
            stack.pop()
        elif len(stack) >= 2 and stack[-1] == ')' and stack[-2] == '(':  # 스택이 2이상존재하고. || 스택 마지막 두번째 (   마지막 ) 인경우 소거함.
            stack.pop()
            stack.pop()
    if not stack:  # 스택이 비어있다면성공
        print("yes")
    else:  # 아니면 균형 X
        print('no')
