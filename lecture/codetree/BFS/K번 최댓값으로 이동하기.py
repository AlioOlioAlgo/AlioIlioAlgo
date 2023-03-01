"""
 *packageName    : 
 * fileName       : K번 최댓값으로 이동하기
 * author         : ipeac
 * date           : 2023-02-26
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2023-02-26        ipeac       최초 생성
"""
from collections import deque

dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
n, k = map(int, input().split())
graph = [
    list(map(int, input().split()))
    for _ in range(n)
]
visited = [
    [False for _ in range(n)]
    for _ in range(n)
]
r, c = map(int, input().split())  # 초기 시작위치
r, c = r - 1, c - 1

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def can_go(x, y):
    if graph[x][y] < first_value and not visited[x][y]:
        return True
    return False

first_value = graph[r][c]

def bfs():
    global first_value, r, c, visited
    
    visited = [
        [False for _ in range(n)]
        for _ in range(n)
    ]
    q = deque()
    result = []
    q.append((r, c))
    visited[r][c] = True
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if in_range(nx, ny) and can_go(nx, ny):
                q.append((nx, ny))
                visited[nx][ny] = True
                if not result:
                    result.append((nx, ny, graph[nx][ny]))
                elif result and result[0][2] < graph[nx][ny]:
                    result.clear()
                    result.append((nx, ny, graph[nx][ny],))
                elif result[0][2] == graph[nx][ny]:
                    result.append((nx, ny, graph[nx][ny]))
    if not result:
        return
    result.sort(key=lambda x: (x[0], x[1]))
    print(f"result  ==> {result}")
    r, c = result[0][0], result[0][1]
    first_value = graph[r][c]

for i in range(k):
    bfs()
print(r + 1, c + 1)
