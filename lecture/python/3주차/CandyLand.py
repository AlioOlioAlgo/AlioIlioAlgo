"""
 *packageName    :
 * fileName       : CandyLand
 * author         : ipeac
 * date           : 2022-12-03
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-12-03        ipeac       최초 생성
 """
from functools import cache

cnt = 0
n = int(input())

arr = [0 for _ in range(n)]
arr[1] = 1

print(f"arr = {arr}")

@cache
def dp(n):
    if n:
        pass

if n == 0:
    print(0)
    exit()
dp(1)
print(cnt)
