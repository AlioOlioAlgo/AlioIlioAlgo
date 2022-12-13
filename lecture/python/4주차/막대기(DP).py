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

sizes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
prices = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
stick_size = int(input())

stick_arr = [i for i in range(1, stick_size + 1)]
print(f"stick_arr = {stick_arr}")
r = {0: 0, 1: 1}

def dp(n, p, r):
    if n not in r.keys():
        if n == 0:
            r[n] = 0
        else:
            r[n] = -1
            for i in range(1, n + 1):
                r[n] = max(r[n], p[i] + dp(n - i, p, r))
    
    return r[n]  # 메모이제이션이 된 값이면 반환하면됨.

print(f"prices = {prices}")
print(dp(stick_size, prices, r))
print(f"r = {r}")
