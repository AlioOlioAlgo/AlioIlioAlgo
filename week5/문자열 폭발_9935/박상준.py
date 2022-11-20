"""
 *packageName    :
 * fileName       : 박상준
 * author         : ipeac
 * date           : 2022-11-17
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-11-17        ipeac       최초 생성
 """
string = input()
bomg = input()
stack = []
for st in string:
    stack.append(st)
    if bomg[-1] == st and ''.join(stack[-len(bomg):]) == bomg:
        for i in range(len(bomg)):
            stack.pop()
if not len(stack):
    print('FRULA')
else:
    print(''.join(stack))
