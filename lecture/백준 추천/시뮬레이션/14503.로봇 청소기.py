"""
 *packageName    : 
 * fileName       : 14503.로봇 청소기
 * author         : ipeac
 * date           : 2023-03-02
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2023-03-02        ipeac       최초 생성
"""
from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
n, m = map(int, input().split())
r, c, d = map(int, input().split())  # 로봇 청소기의 좌표(R, C)  + 로봇 청소기가 바라보는 방향 d
graph = [
    list(map(int, input().split()))
    for _ in range(n)
]
print(f"graph  ==> {graph}")

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

cnt = 0

def bfs():
    global d
    global cnt
    q = deque()
    cnt = 1
    q.append((r, c, d))
    graph[r][c] = 2  # 청소됨
    
    while q:
        x, y, d = q.popleft()
        print(f"x, y, d,  ==> {x, y, d,}")
        for i in range(4):
            nd = (d + 3 - i) % 4
            nx, ny = x + dx[nd], y + dy[nd]
            if in_range(nx, ny) and graph[nx][ny] == 0:  # 4칸중 청소되지 않은 빈 칸이 있는 경우
                q.append((nx, ny, nd))
                graph[nx][ny] = 2  # 청소됨
                cnt += 1
                break
        else:  # 4방향으로 돌아도 갈곳이 없는 경우
            nd = (d + 2) % 4
            nx, ny = x + dx[nd], y + dy[nd]
            if graph[nx][ny] == 1:  # 뒤가 벽이면 stop
                break
            q.append((nx, ny, d))
            graph[nx][ny] = 2  # 청소됨
    print(f"q  ==> {q}")

bfs()
print(cnt)
