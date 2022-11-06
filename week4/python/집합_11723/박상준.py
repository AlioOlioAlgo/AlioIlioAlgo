"""
 *packageName    :
 * fileName       : 박상준
 * author         : ipeac
 * date           : 2022-11-06
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-11-06        ipeac       최초 생성
 """
import sys

input = sys.stdin.readline
m = int(input())
ans = set()
for i in range(m):
    function = input().split()
    if len(function) >= 2:
        num = int(function[1])
    if function[0] == 'add':
        ans.add(num)
    elif function[0] == 'check':
        print(1) if num in ans else print(0)
    elif function[0] == 'remove':
        ans.discard(num)
    elif function[0] == 'toggle':
        if num in ans:
            ans.discard(num)
        else:
            ans.add(num)
    elif function[0] == 'all':
        ans = {i for i in range(1, 21)}
    elif function[0] == 'empty':
        ans.clear()
