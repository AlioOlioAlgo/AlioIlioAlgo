"""
 *packageName    :
 * fileName       : 박상준
 * author         : ipeac
 * date           : 2022-11-25
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-11-25        ipeac       최초 생성
 """
from itertools import combinations

n = int(input())
graph = [
    list(map(int, input().split()))
    for _ in range(n)
]
# print(f"graph = {graph}")
team = set(i for i in range(1, n + 1))
# print(f"team = {team}")
min_value = int(1e9)
for combi in combinations(team, n // 2):
    start = set(combi)
    link = team - start
    start_value = 0
    link_value = 0
    for com in combinations(start, 2):
        start_value += graph[com[0] - 1][com[1] - 1]
        start_value += graph[com[1] - 1][com[0] - 1]
    for com in combinations(link, 2):
        link_value += graph[com[0] - 1][com[1] - 1]
        link_value += graph[com[1] - 1][com[0] - 1]
    min_value = min(min_value, abs(start_value - link_value))
print(min_value)
