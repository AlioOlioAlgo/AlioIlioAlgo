"""
 *packageName    : 
 * fileName       : 상한 귤
 * author         : ipeac
 * date           : 2023-02-28
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2023-02-28        ipeac       최초 생성
 """
from collections import deque

n, k = map(int, input().split())
graph = []
visited = [
    [-2 for _ in range(n)]
    for _ in range(n)
]
for i in range(n):
    line = list(map(int, input().split()))
    graph.append(line)
    for j in range(n):
        if line[j] == 2:
            visited[i][j] = 0
        elif line[j] == 0:
            visited[i][j] = -1

dx, dy = [0, 0, -1, 1], [1, -1, 0, 0]

def can_go(x, y):
    return graph[x][y] == 1 and visited[x][y] != -1

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def bfs(first):
    q = deque()
    q.append((first[0], first[1], 1))
    while q:
        x, y, cnt = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if in_range(nx, ny) and can_go(nx, ny):
                if visited[nx][ny] > cnt or visited[nx][ny] == -2:
                    visited[nx][ny] = cnt
                    q.append((nx, ny, cnt + 1))

for i in range(n):
    for j in range(n):
        if graph[i][j] == 2:
            bfs([i, j])
for i in range(n):
    for j in range(n):
        print(visited[i][j], end=" ")
    print()
