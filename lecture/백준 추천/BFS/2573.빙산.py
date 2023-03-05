"""
 *packageName    : 
 * fileName       : 2573.빙산
 * author         : ipeac
 * date           : 2023-03-05
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2023-03-05        ipeac       최초 생성
"""
import sys
from collections import deque

input = sys.stdin.readline

# 빙산이 두 덩어리 이상으로 분리되는 최초의 시간
n, m = map(int, input().rstrip().split())

graph = [
    list(map(int, input().rstrip().split()))
    for _ in range(n)
]
dx, dy, = [0, 0, 1, -1], [1, -1, 0, 0]

# 그래프안인지 체크
def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

def bfs(x, y):
    q = deque()
    
    q.append((x, y))
    visited[x][y] = True
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if in_range(nx, ny) and not visited[nx][ny]:
                if graph[nx][ny] > 0:
                    q.append((nx, ny))
                    visited[nx][ny] = True

def melt():
    b = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                continue
            for k in range(4):
                nx, ny = i + dx[k], j + dy[k]
                if in_range(nx, ny) and graph[nx][ny] == 0:
                    b[i][j] += 1
    for i in range(n):
        for j in range(m):
            graph[i][j] = max(graph[i][j] - b[i][j], 0)
    return sum([sum(i) for i in graph])  # 남아있는 얼음의 수

ans = 0

while True:
    visited = [[False] * m for _ in range(n)]
    cnt = 0
    for i in range(1, n - 1):
        for j in range(1, m - 1):
            if graph[i][j] != 0 and not visited[i][j]:
                bfs(i, j)
                cnt += 1
    if cnt >= 2:
        print(ans)
        break
    elif cnt == 0:
        print(0)
        break
    if melt() == 0:
        print(0)
        break
    # pprint.pprint(graph, width=50)
    ans += 1
