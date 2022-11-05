"""
 *packageName    :
 * fileName       : 박상준3
 * author         : ipeac
 * date           : 2022-11-02
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-11-02        ipeac       최초 생성
 """
from itertools import combinations

n, m = map(int, input().split())
home = []
chi = []

for i in range(n):
    line = list(map(int, input().split()))
    for j in range(n):
        # 집
        if line[j] == 1:
            home.append([i, j])
        # 치킨집
        elif line[j] == 2:
            chi.append([i, j])

# print(f"n, m = {n, m}")
# print(f"home = {home}")
# print(f"chi = {chi}")
# n, m = (5, 2)
# home = [[0, 3], [1, 0], [1, 2], [3, 3], [3, 4], [4, 3]]
# chi = [[0, 1], [3, 0], [4, 0], [4, 1], [4, 4]]

ans = int(1e9)
for combi in combinations(chi, m):
    tmp = 0
    for ho in home:
        min_chi = int(1e9)
        for i in range(m):  # 치킨
            min_chi = min(min_chi, abs(combi[i][0] - ho[0]) + abs(combi[i][1] - ho[1]))  # 해당 집의 치킨거리
        tmp += min_chi  # 모든 집을 순회하면서 치킨거리를 구한 값을 더한다.
    # 해당값이 최솟값인지 체크한다.
    ans = min(ans, tmp)

print(ans)
