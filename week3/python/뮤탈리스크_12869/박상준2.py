"""
 *packageName    :
 * fileName       : 박상준2
 * author         : ipeac
 * date           : 2022-11-08
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-11-08        ipeac       최초 생성
 """
import sys
from itertools import permutations

n = 3
scv = [12, 10, 4]

# n 이 3보다 작은 경우 인덱스 에러 방지
if n < 3:
    scv += [0] * (3 - n)
attacks = [9, 3, 1]
# 각 체력에 따른 공격 횟수를 저장한 리스트 dp에 담는다.
dp = [[[-1 for _ in range(61)] for _ in range(61)] for _ in range(61)]

# 재귀를 통해 (12,10,4) -> hp_update(3,3,7)
# dp[12][10][4] = -1 -> sys.maxsize
# dp[3][7][3] = -1 -> sys.maxsize
# hp_update(-6,4,2) return hp_update(0,4,2)
# hp_update(0,4,2) -> dp[0][4][2] = sys.maxsize
#
def hp_update(a, b, c):
    if a < 0:
        return hp_update(0, b, c)
    if b < 0:
        return hp_update(a, 0, c)
    if c < 0:
        return hp_update(a, b, 0)
    if not a and not b and not c:
        return 0
    if dp[a][b][c] != -1:  # 방문되었는지 아닌지 체크하는 역할인듯
        return dp[a][b][c]
    dp[a][b][c] = sys.maxsize
    # 3가지 공격을 a,b,c, 골고루 해준다.
    for dmg in list(permutations(attacks)):
        dp[a][b][c] = min(dp[a][b][c], hp_update(a - dmg[0], b - dmg[1], c - dmg[2]))
    dp[a][b][c] += 1
    return dp[a][b][c]

print(hp_update(scv[0], scv[1], scv[2]))
