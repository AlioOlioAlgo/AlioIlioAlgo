"""
 *packageName    : 
 * fileName       : 박상준
 * author         : ipeac
 * date           : 2022-10-22
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-10-22        ipeac       최초 생성
 """

from collections import deque

dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]  # 우 좌 하 상

n, m = map(int, input().split())
graph = [
    list(map(int, input()))
    for _ in range(n)
]

# print(f"n, m = {n, m}")
# print(f"graph = {graph}")

# n, m = (4, 6)
# graph = [[1, 0, 1, 1, 1, 1], [1, 0, 1, 0, 1, 0], [1, 0, 1, 0, 1, 1], [1, 1, 1, 0, 1, 1]]

def bfs(i, j):
    visited = [[0] * m for _ in range(n)]
    q = deque()
    q.append([i, j])
    visited[i][j] = 1
    
    while q:
        x, y = q.popleft()
        for xx, yy in zip(dx, dy):
            nx = xx + x
            ny = yy + y
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and graph[nx][ny] == 1:
                q.append([nx, ny])
                visited[nx][ny] = visited[x][y] + 1
    return visited[n - 1][m - 1]

def dfs(x, y, visited):
    for xx, yy in zip(dx, dy):
        nx = xx + x
        ny = yy + y
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if graph[nx][ny] == 1 and visited[nx][ny] == 0:
            visited[nx][ny] = visited[x][y] + 1
            dfs(nx, ny, visited)
    return visited[n - 1][m - 1]

visited = [[0] * m for _ in range(n)]
print(dfs(0, 0, visited) + 1)
# dfs 의 경우 맹목적인 탐색이기에
# 최단거리 탐색의 경우 틀릴수도있고 맞을 수도있기에
# 정답을 구하기가 어렵다고 한다,.
