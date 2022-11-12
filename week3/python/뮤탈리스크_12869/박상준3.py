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

n = int(input())
scv = list(map(int, input().split()))

attack = [9, 3, 1]
hp = [[[61] * 61 for _ in range(61)] for _ in range(61)]
if len(scv) < 3:
    scv += [0] * (3 - n)

def dfs(x, y, z):
    if x <= 0 and y <= 0 and z <= 0:
        return 0
    if x < 0:
        x = 0
    if y < 0:
        y = 0
    if z < 0:
        z = 0
    if hp[x][y][z] < 61: return hp[x][y][z]
    for i, j, k in attack_case:
        hp[x][y][z] = min(dfs(x - i, y - j, z - k) + 1, hp[x][y][z])
    return hp[x][y][z]

attack_case = list(permutations(attack))  # scv에 순차적으로 데미지를 줄 순열

print(dfs(scv[0], scv[1], scv[2]))
