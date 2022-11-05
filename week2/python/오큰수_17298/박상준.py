"""
 *packageName    :
 * fileName       : 박상준
 * author         : ipeac
 * date           : 2022-10-27
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-10-27        ipeac       최초 생성
 """
from collections import deque

# n = int(input())

# a = list(map(int, input().split()))

# print(f"ans = {ans}")
# print(f"n = {n}")
# print(f"a = {a}")

# ans = [-1, -1, -1, -1]
n = 4
a = deque([3, 5, 2, 7])
ans = [-1] * n

stack = deque()
for i in range(n):
    while stack and stack[-1][0] < a[i]:
        print(f"stack = {stack}")
        value, idx = stack.pop()
        ans[idx] = a[i]
    stack.append([a[i], i])
print(*ans)
