"""
 *packageName    : 
 * fileName       : 박상준
 * author         : ipeac
 * date           : 2022-10-23
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-10-23        ipeac       최초 생성
 """
import sys
from collections import deque

sys.setrecursionlimit(10 ** 6)

dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
n = int(input())
graph = []
max_value = 0
for i in range(n):
    input_value = list(map(int, input().split()))
    graph.append(input_value)
    max_value = max(max_value, max(input_value))

# graph = [[6, 8, 2, 6, 2], [3, 2, 3, 4, 6], [6, 7, 3, 3, 2], [7, 2, 5, 3, 6], [8, 9, 5, 2, 7]]

def bfs(i, j, deep):
    visited[i][j] = 1
    q = deque([(i, j)])
    
    while q:
        x, y = q.popleft()
        for xx, yy, in zip(dx, dy):
            nx, ny = xx + x, yy + y
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and graph[nx][ny] > deep:
                q.append((nx, ny))
                visited[nx][ny] = 1

def dfs(x, y, deep):
    visited[x][y] = 1
    for xx, yy in zip(dx, dy):
        nx, ny = xx + x, yy + y
        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and graph[nx][ny] > deep:
            dfs(nx, ny, deep)

ans = 0
for j_value in range(max_value):
    visited = [[0] * n for _ in range(n)]
    max_cnt = 0
    for i in range(n):
        for j in range(n):
            # 2 이하인 부분은 다 잠겼으니 접근 X 방문 x 하고 2 초과인 부분만 접근할수있다.
            if graph[i][j] > j_value and not visited[i][j]:
                dfs(i, j, j_value)
                max_cnt += 1
    ans = max(ans, max_cnt)

print(ans)
