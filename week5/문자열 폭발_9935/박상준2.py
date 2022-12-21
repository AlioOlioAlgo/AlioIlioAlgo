"""
 *packageName    :
 * fileName       : 박상준2
 * author         : ipeac
 * date           : 2022-12-13
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-12-13        ipeac       최초 생성
 """
string = input()
explosion_string = list(input())
stack = []
for value in string:
    stack.append(value)
    if len(stack) >= len(explosion_string) and value == explosion_string[-1] and stack[-len(explosion_string):] == explosion_string:  # 해당 문자가 폭발문자열의 마지막에 위치하며, 폭발문자열의 길이만큼 stack을 꺼낸 값이 폭발문자열과 일치한다면 스택에서 제외시킨다.
        for i in range(len(explosion_string)):
            stack.pop()
if not stack:
    print("FRULA")
else:
    print(''.join(stack))
