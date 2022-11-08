"""
 *packageName    :
 * fileName       : 박상준
 * author         : ipeac
 * date           : 2022-11-07
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-11-07        ipeac       최초 생성
 """
from collections import deque
from itertools import combinations

n = int(input())
population = list(map(int, input().split()))
graph = [[] for _ in range(n + 1)]
for i in range(n):
    info = list(map(int, input().split()))
    for j in range(1, info[0] + 1):
        graph[i + 1].append(info[j])

# print(f"n = {n}")
# print(f"population = {population}")
# print(f"graph = {graph}")

# n = 6
# population = [5, 2, 3, 4, 1, 2]
# graph = [[], [2, 4], [1, 3, 6, 5], [4, 2], [1, 3], [2], [2]]

# bfs를 돌아서 이어지는 지 체크함과 동시에 인구수 체크
def bfs(num_list):
    _sum = 0
    # 첫번째 값을 돌면서 갈수있는 모든 경우의 수 고려
    start = num_list[0]
    q = deque()
    q.append(start)
    # start
    visited = [start]
    # 인구수 더하기 + visited 로 방문한 길이 체크
    while q:
        x = q.popleft()
        # 인구를 하나씩 더해간다.
        _sum += population[x - 1]
        for v in graph[x]:
            # v in num_list 로 해당 값에만 존재하는 값으로만 이동가능하다는 제약조건
            if v not in visited and v in num_list:
                visited.append(v)
                q.append(v)
    return _sum, len(visited)

min_diff = int(1e9)
# 절반만 구해도 나머지 선거구 자동 확정
for i in range(1, n // 2 + 1):
    for combi in combinations(range(1, n + 1), i):
        # if combi == (1, 3, 4):
        sum_a, len_a = bfs(combi)
        sum_b, len_b, = bfs([i for i in range(1, n + 1) if i not in combi])
        if len_a + len_b == n:  # 모든 노드 방문 성공
            min_diff = min(min_diff, abs(sum_a - sum_b))
if min_diff == int(1e9):
    print(-1)
else:
    print(min_diff)
