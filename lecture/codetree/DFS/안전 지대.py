"""
 *packageName    : 
 * fileName       : 안전 지대
 * author         : ipeac
 * date           : 2023-02-15
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2023-02-15        ipeac       최초 생성
"""
import sys

sys.setrecursionlimit(10 ** 5)
n, m, = map(int, input().split())
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
graph = [
    list(map(int, input().split()))
    for _ in range(n)
]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

def dfs(x, y):
    global cnt
    for xx, yy in zip(dx, dy):
        nx, ny = xx + x, yy + y
        if in_range(nx, ny) and graph[nx][ny] > k and not visited[nx][ny]:
            visited[nx][ny] = True
            dfs(nx, ny)

ans = -1e9
k = 1
k_tmp = 1
check_it = True
while check_it:
    visited = [
        [False for _ in range(m)]
        for _ in range(n)
    ]
    check_it = False
    cnt = 0
    
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and graph[i][j] > k:
                check_it = True
                cnt += 1
                visited[i][j] = True
                dfs(i, j)
    if ans < cnt:
        k_tmp = k
        ans = cnt
    k += 1

print(k_tmp, ans)
