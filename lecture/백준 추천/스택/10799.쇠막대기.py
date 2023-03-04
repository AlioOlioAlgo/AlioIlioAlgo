"""
 *packageName    : 
 * fileName       : 10799.쇠막대기
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
stack = []
bar = list(map(str, input().rstrip()))
ans = 0
for i in range(len(bar)):
    if bar[i] == '(':
        stack.append(bar[i])
    else:
        if bar[i - 1] == '(':
            stack.pop()
            ans += len(stack)
        else:
            stack.pop()
            ans += 1
print(ans)
