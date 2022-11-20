"""
 *packageName    :
 * fileName       : 박상준
 * author         : ipeac
 * date           : 2022-10-28
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-10-28        ipeac       최초 생성
 """
import sys
from collections import deque

input = sys.stdin.readline

n, l, r = map(int, input().split())
world = [
    list(map(int, input().split()))
    for _ in range(n)
]

dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]

# n, l, r = (2, 20, 50)
# world = [[50, 30], [20, 40]]

def bfs(i, j):
    total_population, total_cnt = world[i][j], 1
    index_repo = [[i, j]]
    q = deque([[i, j]])
    visited[i][j] = 1
    while q:
        x, y = q.popleft()
        for xx, yy in zip(dx, dy):
            nx, ny = xx + x, yy + y
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and l <= abs(world[x][y] - world[nx][ny]) <= r:
                q.append([nx, ny])
                visited[nx][ny] = 1
                total_population += world[nx][ny]
                total_cnt += 1
                index_repo.append([nx, ny])
    if total_cnt != 1:
        return index_repo, total_population, total_cnt
    else:
        return -1, -1, -1

day = 0
while True:
    max_cnt = -1
    visited = [[0] * n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                index_repo_i, total_population_i, total_cnt_i, = bfs(i, j)
                max_cnt = max(max_cnt, total_cnt_i)
                if total_cnt_i < 2:
                    continue
                value = total_population_i // total_cnt_i
                for index in index_repo_i:
                    world[index[0]][index[1]] = value
    if max_cnt == -1:
        break
    day += 1
print(day)
