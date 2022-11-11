"""
 *packageName    :
 * fileName       : 박상준3
 * author         : ipeac
 * date           : 2022-11-11
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-11-11        ipeac       최초 생성
 """
from itertools import permutations

n = 3
scv = [4, 10, 12]
scv = sorted(scv + [0] * (3 - n))  # 조로려~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print(f"scv = {scv}")
attack = [9, 3, 1]
hp = [[[0] * 61 for _ in range(61)] for _ in range(61)]
if len(scv) < 3:
    scv += [0] * (3 - n)

def dfs(x, y, z):
    if x == 0 and y == 0 and z == 0:
        return 0
    if hp[x][y][z]:
        return hp[x][y][z]
        
        pass

attack_case = list(permutations(attack, 3))  # scv에 순차적으로 데미지를 줄 순열
print(f"attack_case = {attack_case}")

print(dfs(scv[0], scv[1], scv[2]))
