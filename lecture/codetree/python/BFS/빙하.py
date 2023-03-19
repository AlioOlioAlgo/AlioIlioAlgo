"""
 *packageName    : 
 * fileName       : 빙하
 * author         : ipeac
 * date           : 2023-02-26
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2023-02-26        ipeac       최초 생성
"""
import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
graph = [
    list(map(int, input().rstrip().split()))
    for _ in range(n)
]
visited = []
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
ans = 0
last = 0

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

def chcek_one():
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                return True
    return False

def bfs():
    global visited, last, ans
    visited = [
        [False for _ in range(m)]
        for _ in range(n)
    ]
    result = set()
    q = deque()
    q.append((0, 0))
    visited[0][0] = True
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if in_range(nx, ny):
                if not visited[nx][ny]:
                    if graph[nx][ny] == 1:
                        result.add((nx, ny))
                    else:
                        q.append((nx, ny))
                        visited[nx][ny] = True
    last = len(result)
    ans += 1
    for x, y in result:
        graph[x][y] = 0

while chcek_one():
    bfs()
print(ans, last)
