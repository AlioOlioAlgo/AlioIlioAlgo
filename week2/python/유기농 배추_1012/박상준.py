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
# t = int(input())
# for _ in range(t):
# m, n, k = map(int, input().split())
# print(f"m,n,k = {m, n, k}")
import sys
from collections import deque

dx, dy = [0, 0, 1, -1], [1, -1, 0, 0],

sys.setrecursionlimit(10 ** 8)

for _ in range(t := int(input())):
    m, n, k = map(int, input().split())
    
    graph = [
        [0] * m
        for _ in range(n)
    ]
    for _ in range(k):
        y, x = map(int, input().split())
        graph[x][y] = 1
    print(f"graph = {graph}")
    visited = [[0] * m for _ in range(n)]
    
    def dfs(x_1, y_1):
        visited[x_1][y_1] = 1
        for xx, yy in zip(dx, dy):
            nx, ny = xx + x_1, yy + y_1
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
                visited[nx][ny] = 1
                dfs(nx, ny)
    
    def bfs(i, j):
        global visited
        visited[i][j] = 1
        q = deque([[i, j]])
        
        while q:
            x, y = q.popleft()
            for xx, yy in zip(dx, dy):
                nx, ny = xx + x, yy + y
                if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and graph[nx][ny] == 1:
                    q.append([nx, ny])
                    visited[nx][ny] = 1
    
    #
    cnt = 0
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and graph[i][j] == 1:
                dfs(i, j)
                cnt += 1
    print(cnt)
