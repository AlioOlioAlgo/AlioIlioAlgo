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
import sys

sys.setrecursionlimit(10 ** 5)
n = int(input())

target = 4
if n < 4:
    target = n
number_arr = [i for i in range(1, target + 1)]
cnt = 0

def dp(n):
    global cnt
    # print(f"n = {n}")
    # if not n:
    #     cnt += 1
    #     return
    #
    # for num in number_arr:
    #     if n - num >= 0:
    #         dp(n - num)
    cnt = 0
    dp_sub(n)
    return cnt

def dp_sub(n):
    global cnt
    print(f"n = {n}")
    if not n:
        cnt += 1
        return
    
    for num in number_arr:
        if n - num >= 0:
            dp_sub(n - num)

if n == 0:
    print(0)
    exit()

# print(int(math.pow(2, n - 1)))
# dp(n)  # 테스트 케이스 체크를 위한 함수 n= 5
print(dp(n))
# dp(1)
# print(cnt)
