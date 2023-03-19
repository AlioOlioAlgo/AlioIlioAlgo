"""
 *packageName    : 
 * fileName       : 2206.벽 부수고 이동하기
 * author         : ipeac
 * date           : 2023-03-07
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2023-03-07        ipeac       최초 생성
"""
from collections import deque

n, m = map(int, input().split())

graph = [
    list(map(int, input()))
    for _ in range(n)
]

dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

ans = 1e9

def bfs():
    global ans
    visited = [
        [[0] * 2 for _ in range(m)]
        for _ in range(n)
    ]
    visited[0][0][0] = 1
    q = deque()
    q.append((0, 0, 0))
    while q:
        x, y, z = q.popleft()
        if x == n - 1 and y == m - 1:
            return visited[x][y][z]
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if in_range(nx, ny):
                if graph[nx][ny] == 1 and z == 0:  # 벽이 있는 데 아직 벽을 부순적 없는 경우
                    visited[nx][ny][1] = visited[x][y][0] + 1
                    q.append((nx, ny, 1))
                elif graph[nx][ny] == 0 and visited[nx][ny][z] == 0:  # 벽이 없는 경우
                    visited[nx][ny][z] = visited[x][y][z] + 1
                    q.append((nx, ny, z))
    return -1

print(bfs())
