"""
 *packageName    :
 * fileName       : 삼각형 컨베이어 벨트
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
long = deque()
for _ in range(3):
    long.extend(list(map(int, input().split())))
# print(f"long = {long}")

for i in range(t):
    long.rotate(1)
while len(long):
    for i in range(n):
        print(long.popleft(), end=" ")
    print()
