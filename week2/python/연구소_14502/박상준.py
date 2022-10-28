"""
 *packageName    : 
 * fileName       : 박상준
 * author         : ipeac
 * date           : 2022-10-25
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-10-25        ipeac       최초 생성
 """
import copy
from collections import deque

n, m = map(int, input().split())
graph = [
    list(map(int, input().split()))
    for _ in range(n)
]
# print(f"n,m = {n, m}")
# print(f"graph = {graph}")


dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]

# n, m = (7, 7)
# graph = [[2, 0, 0, 0, 1, 1, 0], [0, 0, 1, 0, 1, 2, 0], [0, 1, 1, 0, 1, 0, 0], [0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 1], [0, 1, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0]]
answer = 0

def bfs():
    q = deque()
    tmp_graph = copy.deepcopy(graph)
    for i in range(n):
        for j in range(m):
            if tmp_graph[i][j] == 2:
                q.append([i, j])
    while q:
        x, y = q.popleft()
        for xx, yy in zip(dx, dy):
            nx, ny = xx + x, yy + y
            if 0 <= nx < n and 0 <= ny < m and tmp_graph[nx][ny] == 0:
                tmp_graph[nx][ny] = 2
                q.append([nx, ny])
    cnt = 0
    for i in range(n):
        cnt += tmp_graph[i].count(0)
    global answer
    answer = max(answer, cnt)

def make_wall(start_row, start_col, cnt):
    if cnt == 3:
        bfs()
        return
    for i in range(start_row, n):
        for j in range(start_col, m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                make_wall(i, j + 1, cnt + 1)
                graph[i][j] = 0
        start_col = 0

make_wall(0, 0, 0)
print(answer)
