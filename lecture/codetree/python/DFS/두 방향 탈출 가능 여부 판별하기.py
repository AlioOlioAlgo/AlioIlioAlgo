"""
 *packageName    : 
 * fileName       : 그리드 상에서의 DFS 탐색
 * author         : ipeac
 * date           : 2023-02-14
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2023-02-14        ipeac       최초 생성
"""
import sys

n, m = map(int, input().split())
# 아래 오른쪽으로만 가능
dx = [1, 0]
dy = [0, 1]
graph = [
    list(map(int, input().split()))
    for _ in range(n)
]
# print(f"graph  ==> {graph}")
visited = [
    [False for _ in range(m)]
    for _ in range(n)
]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

def check(x, y):
    if in_range(x, y) and graph[x][y] == 1 and not visited[x][y]:
        return True
    return False

def dfs(x, y):
    if x == n - 1 and y == m - 1:
        print(1)
        sys.exit(0)
    visited[x][y] = True
    
    for xx, yy in zip(dx, dy):
        nx, ny = xx + x, yy + y
        print(f"nx,ny  ==> {nx, ny}")
        if check(nx, ny):
            dfs(nx, ny)

dfs(0, 0)
print(0)
