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
import math
from itertools import product

# cnt = 0
n = int(input())

# arr = [0 for _ in range(n)]
# arr[1] = 1
# arr[2] = 2
# arr[3] = 4
# arr[4] = 8
# arr[5] = 16
# arr[6] = 32
# arr[7] = 64

# print(f"arr = {arr}")

def make_distinct_arr(target):
    tmp = [i for i in range(1, target + 1)]
    cnt = 0
    for i in range(1, target + 1):
        for combi in product(tmp, repeat=i):
            if sum(combi) == target:
                cnt += 1
                print(f"combi = {combi}")
    print(f"cnt = {cnt}")

if n == 0:
    print(0)
    exit()
print(int(math.pow(2, n - 1)))
# make_distinct_arr(n)  # 테스트 케이스 체크를 위한 함수
# dp(1)
# print(cnt)
