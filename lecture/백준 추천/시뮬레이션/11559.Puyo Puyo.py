"""
 *packageName    : 
 * fileName       : 11559.Puyo Puyo
 * author         : ipeac
 * date           : 2023-03-14
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2023-03-14        ipeac       최초 생성
"""
from collections import deque

graph = [
    list(map(str, input()))
    for _ in range(12)
]
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]

def in_range(x, y):
    return 0 <= x < 12 and 0 <= y < 6

visited = [
    [False for _ in range(6)]
    for _ in range(12)
]

def bfs(x, y):
    global visited
    q = deque()
    q.append((x, y))
    result.append((x, y))
    visited[x][y] = True
    first = graph[x][y]
    cnt = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if in_range(nx, ny) and not visited[nx][ny] and first == graph[nx][ny]:
                q.append((nx, ny))
                result.append((nx, ny))
                visited[nx][ny] = True
                cnt += 1
    if cnt < 4:
        for i in range(cnt):
            result.pop()

result = []

def down():
    for i in range(6):
        for j in range(10, -1, -1):
            for k in range(11, j, -1):
                if graph[j][i] != '.' and graph[k][i] == '.':
                    graph[k][i] = graph[j][i]
                    graph[j][i] = '.'
                    break

ans = 0

def bomb(x, y):
    global visited, result, ans
    visited = [
        [False for _ in range(6)]
        for _ in range(12)
    ]
    result = []
    for i in range(12):
        for j in range(6):
            if graph[i][j] != '.' and not visited[i][j]:
                bfs(i, j)
    if len(result) == 0:
        return False
    else:
        ans += 1
    for re in result:
        graph[re[0]][re[1]] = '.'
    down()
    return True

while True:
    boolean = bomb(0, 0)
    if not boolean:
        break
print(ans)
