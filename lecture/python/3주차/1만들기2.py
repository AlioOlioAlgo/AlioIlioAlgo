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
from functools import cache

n = int(input())
arr = [int(1e9)] * (n + 1)

@cache
def dp(n, cnt):
    print(f"arr = {arr}")
    print("==========================================")
    print(f"cnt = {cnt}")
    print(f"n = {n}")
    if n == 1:
        arr[n] = min(arr[n], cnt)
        return arr[n]
    arr[n] = cnt
    
    if not n % 3:
        dp(n // 3, cnt + 1)
    if not n % 2:
        dp(n // 2, cnt + 1)
    dp(n - 1, cnt + 1)

dp(n, 0)
print("=====================정답=====================")
print(arr[1])
