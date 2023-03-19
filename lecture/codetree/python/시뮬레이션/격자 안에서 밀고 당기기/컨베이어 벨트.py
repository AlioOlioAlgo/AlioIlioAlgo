"""
 *packageName    :
 * fileName       : 컨베이어 벨트
 * author         : ipeac
 * date           : 2022-12-30
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-12-30        ipeac       최초 생성
 """
from collections import deque

n, t = map(int, input().split())
init = list(map(int, input().split()))
next = list(map(int, input().split()))
long = init + next
# print(f"long = {long}")
long = deque(long)
# t 초 뒤의 컨베이어 벨트를
for i in range(t):
    long.rotate(1)
while len(long):
    for i in range(n):
        print(long.popleft(), end=" ")
    print()
