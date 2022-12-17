"""
 *packageName    :
 * fileName       : 막대기(DP)
 * author         : ipeac
 * date           : 2022-12-13
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-12-13        ipeac       최초 생성
 """

prices = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
stick_size = int(input())

stick_arr = [i for i in range(1, stick_size + 1)]
# print(f"stick_arr = {stick_arr}")
r = {0: 0, 1: 1}  # dp 메모이제이션

def dp(n, prices, r):
    # print("==========================================")
    # print(f"n = {n}")
    if n not in r.keys():
        if n == 0:
            r[n] = 0
        else:
            r[n] = -1
            for i in range(1, n + 1):
                r[n] = max(r[n], prices[i] + dp(n - i, prices, r))  # 처음에 dp(1) = 1 반환 =>
                # print(f"p[i] = {p[i]}")
                # print(f"dp(n - i, p, r) = {dp(n - i, p, r)}")
                # print(f"r[n] = {r[n]}")
    
    return r[n]  # 메모이제이션이 된 값이면 반환하면됨.

print(f"prices = {prices}")
print(dp(stick_size, prices, r))
print(f"r = {r}")
