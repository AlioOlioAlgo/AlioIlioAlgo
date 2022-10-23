"""
 *packageName    : 
 * fileName       : 박상준
 * author         : ipeac
 * date           : 2022-10-23
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-10-23        ipeac       최초 생성
 """

# m : 세로 n 가로
import sys
from collections import deque

dx, dy = [0, 0, 1, -1], [1, -1, 0, 0],

sys.setrecursionlimit(10 ** 6)

# m, n, k = (5, 7, 3)
# graph = [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]
# rec = [[0, 2, 4, 4], [1, 1, 2, 5], [4, 0, 6, 2]]

m, n, k = map(int, input().split())
graph = [
    [0] * n
    for _ in range(m)
]

rec = [
    list(map(int, input().split()))
    for _ in range(k)
]

for value in rec:
    y1, x1, y2, x2 = map(int, value)
    for x in range(x1, x2):
        for y in range(y1, y2):
            graph[x][y] = 1

def bfs(i, j):
    weight = 1
    visited[i][j] = 1
    q = deque([[i, j]])
    
    while q:
        x, y = q.popleft()
        for xx, yy in zip(dx, dy):
            nx, ny = xx + x, yy + y
            if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny] and graph[nx][ny] == 0:
                q.append([nx, ny])
                visited[nx][ny] = 1
                weight += 1
    return weight

def dfs(i, j):
    global weight
    
    for xx, yy in zip(dx, dy):
        nx, ny = xx + i, yy + j
        if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny] and graph[nx][ny] == 0:
            visited[nx][ny] = 1
            weight += 1
            dfs(nx, ny)
    if weight == 0:
        return 1
    
    return weight

cnt = 0
ans = []
visited = [[0] * n for _ in range(m)]

for i in range(m):
    for j in range(n):
        if not visited[i][j] and graph[i][j] == 0:
            weight = 0
            ans.append(dfs(i, j))
            cnt += 1

print(cnt)
print(*sorted(ans))
