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

n = int(input())
arr = {1: 0}

def dp(n):
    print(f"arr = {arr}")
    print("==========================================")
    print(f"n = {n}")
    if n in arr.keys():
        return arr[n]
    if not n % 3:
        arr[n] = min(dp(n - 1) + 1, dp(n // 3) + 1)
    elif not n % 2:
        arr[n] = min(dp(n - 1) + 1, dp(n // 2) + 1)
    else:
        arr[n] = dp(n - 1) + 1
    return arr[n]

print(dp(n))
print("=====================정답=====================")
