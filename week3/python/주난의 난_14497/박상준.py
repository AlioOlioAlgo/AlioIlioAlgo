"""
 *packageName    :
 * fileName       : 박상준
 * author         : ipeac
 * date           : 2022-11-03
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-11-03        ipeac       최초 생성
 """
from collections import deque

n, m = map(int, input().split())
x1, y1, x2, y2 = map(int, input().split())

graph = [
    list(map(str, input()))
    for _ in range(n)
]
# n, m = (5, 7)
# x1, y1, x2, y2 = (3, 4, 1, 2)
# graph = [['1', '#', '1', '0', '1', '1', '1'], ['1', '1', '0', '1', '0', '0', '1'], ['0', '0', '1', '*', '1', '1', '1'], ['1', '1', '0', '1', '1', '1', '1'], ['0', '0', '1', '1', '0', '0', '1']]

dx, dy = [0, 0, 1, -1], [1, -1, 0, 0],
distance = [[-1] * m for _ in range(n)]

def bfs(i, j):
    q = deque()
    q.append([i, j])
    distance[i][j] = 0
    
    while q:
        x, y = q.popleft()
        
        for xx, yy, in zip(dx, dy):
            nx, ny = xx + x, yy + y
            if 0 <= nx < n and 0 <= ny < m and distance[nx][ny] == -1:
                if graph[nx][ny] == '1' or graph[nx][ny] == '#':
                    distance[nx][ny] = distance[x][y] + 1
                    q.append([nx, ny])
                elif graph[nx][ny] == '0':
                    distance[nx][ny] = distance[x][y]
                    q.appendleft([nx, ny])  # 이거 이유를 모르겠음

bfs(x1 - 1, y1 - 1)
print(distance[x2 - 1][y2 - 1])
