"""
 *packageName    : 
 * fileName       : 박상준
 * author         : ipeac
 * date           : 2022-10-25
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-10-25        ipeac       최초 생성
 """
from collections import deque

# 세로 가로 길이
m, n = map(int, input().split())
graph = [
    list(map(int, input().split()))
    for _ in range(m)
]
# print(f"m,n = {m, n}")
# print(f"graph = {graph}")

dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]

# m, n = (13, 12)
# graph = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0], [0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0], [0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0],
#          [0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0], [0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0], [0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0], [0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0], [0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0], [0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
#          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
cheese = []

# 겉돌기 가다가 1 만나면 큐에 담지않고 0으로 바꿔주기만 한다. > 나머지 순회
def bfs(i, j):
    q = deque([[i, j]])
    visited = [[0] * n for _ in range(m)]
    visited[i][j] = 1
    cnt = 0
    while q:
        x, y = q.popleft()
        for xx, yy in zip(dx, dy):
            nx, ny = xx + x, yy + y
            if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                if graph[nx][ny] == 0:
                    visited[nx][ny] = 1
                    q.append([nx, ny])
                elif graph[nx][ny] == 1:
                    visited[nx][ny] = 1
                    cnt += 1
                    graph[nx][ny] = 0
    cheese.append(cnt)
    return cnt

ans = 0
while True:
    ans += 1
    if bfs(0, 0) == 0:
        break
print(ans - 1)
print(cheese[-2])  # 마지막 전단계 cnt 출력
