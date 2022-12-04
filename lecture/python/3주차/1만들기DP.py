"""
 *packageName    :
 * fileName       : 1만들기DP
 * author         : ipeac
 * date           : 2022-12-03
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-12-03        ipeac       최초 생성
 """
import time
from functools import cache

@cache
def dp(n, cnt):
    print("==========================================")
    print(f"cnt = {cnt}")
    print(f"n = {n}")
    if n == 1:
        print(cnt)
        end = time.time()
        print(f"{end - start:.5f}sec")
        exit()
    if not n % 3:
        dp(n // 3, cnt + 1)
    if not n % 2:
        dp(n // 2, cnt + 1)
    dp(n - 1, cnt + 1)

start = time.time()
n = int(input())
print(dp(n, 0))
