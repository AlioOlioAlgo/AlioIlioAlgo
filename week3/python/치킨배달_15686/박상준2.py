"""
 *packageName    : 
 * fileName       : 박상준2
 * author         : ipeac
 * date           : 2022-11-01
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-11-01        ipeac       최초 생성
"""
from collections import deque
from itertools import combinations

n, m = map(int, input().split())
graph = [
    list(map(int, input().split()))
    for _ in range(n)
]
# print(f"n,m = {n, m}")
# print(f"graph = {graph}")

# n, m = (5, 2)
# graph = [[0, 2, 0, 1, 0], [1, 0, 1, 0, 0], [0, 0, 0, 0, 0], [2, 0, 0, 1, 1], [2, 2, 0, 1, 2]]
# 빈칸 0
# 1 집 # 2 치킨
chi = deque()
home = deque()

for i in range(n):
    for j in range(n):
        if graph[i][j] == 2:
            chi.append([i, j])
        elif graph[i][j] == 1:
            home.append([i, j])

ans = int(1e9)  # 조합 중에 치킨 거리의 최솟값을 담아야합니다.

for combi in combinations(chi, m):
    print(f"combi = {combi}")
    max_value = 0
    
    for ho in home:
        temp_min = int(1e9)  # 임의의 최솟값
        for j in range(m):
            # 한 치킨집과 특정 집과의 거리들 중에 제일 작은 값을 담아야합니다.
            temp_min = min(temp_min, abs(ho[0] - combi[j][0]) + abs(ho[1] - combi[j][1]))
        
        # 한 치킨집과 특정 집과의 거리들 중에 제일 작은 값인 temp_min을 max_value 에 담습니다.
        max_value += temp_min
    # 맥스 밸류는 해당 조합의 치킨거리들의 합의 최솟값이 됩니다.
    ans = min(ans, max_value)

print(ans)
