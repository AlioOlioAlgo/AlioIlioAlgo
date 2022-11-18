"""
 *packageName    :
 * fileName       : 박상준2
 * author         : ipeac
 * date           : 2022-11-18
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-11-18        ipeac       최초 생성
 """
from collections import deque

dx, dy = [0, 0, 1, - 1], [1, -1, 0, 0]
m, n = map(int, input().split())
graph = [
    list(map(str, input()))
    for _ in range(m)
]

def bfs(i, j):
    visited = [[0] * n
               for _ in range(m)]
    visited[i][j] = 1
    q = deque()
    q.append((i, j))
    
    while q:
        x, y = q.popleft()
        for xx, yy in zip(dx, dy):
            nx, ny = xx + x, yy + y
            if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny] and graph[nx][ny] == 'L':
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny))
    return max(map(max, visited))

max_dist = 0
for i in range(m):
    for j in range(n):
        if graph[i][j] == 'L':
            max_dist = max(max_dist, bfs(i, j))
print(max_dist - 1)
