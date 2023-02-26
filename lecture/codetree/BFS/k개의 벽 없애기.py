"""
 *packageName    : 
 * fileName       : k개의 벽 없애기
 * author         : ipeac
 * date           : 2023-02-26
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2023-02-26        ipeac       최초 생성
"""
import itertools
import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().rstrip().split())
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]

graph = [
]
walls = set()
for i in range(n):
    line = list(map(int, input().rstrip().split()))
    graph.append(line)
    for j in range(n):
        if line[j] == 1:
            walls.add((i, j))

sx, sy = map(int, input().rstrip().split())
ex, ey = map(int, input().rstrip().split())
sx, sy = sx - 1, sy - 1
ex, ey = ex - 1, ey - 1

combi = list(itertools.combinations(walls, k))

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

min_time = 1e9

def bfs():
    global min_time
    q = deque()
    ans = 1
    q.append((sx, sy))
    visited = [
        [0 for _ in range(n)]
        for _ in range(n)
    ]
    visited[sx][sy] = 0
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if (nx, ny) == (ex, ey):
                min_time = min(visited[x][y] + 1, min_time)
                return
            if in_range(nx, ny) and graph[nx][ny] == 0 and not visited[nx][ny]:
                q.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1

for i in range(len(combi)):
    for j in range(k):
        graph[combi[i][j][0]][combi[i][j][1]] = 0
    
    bfs()
    for j in range(k):
        graph[combi[i][j][0]][combi[i][j][1]] = 1

print(-1 if min_time == 1e9 else min_time)
