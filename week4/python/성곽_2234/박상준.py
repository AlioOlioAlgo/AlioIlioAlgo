"""
 *packageName    :
 * fileName       : 박상준
 * author         : ipeac
 * date           : 2022-11-13
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-11-13        ipeac       최초 생성
 """
# 1. 방의 개수
# 2. 가장 넓은 방의 크기
# 3. 하나의 벽을 제거하여 얻을 수 있는 방의 최대 크기
from collections import deque

n, m = map(int, input().split())
graph = [
    list(map(int, input().split()))
    for _ in range(m)
]
# 남 동  북 서
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
# print(f"n,m = {n, m}")
# print(f"graph = {graph}")
visited = [[0] * n for _ in range(m)]
max_room = 0

def bfs(row, col):
    q = deque()
    q.append([row, col])
    visited[row][col] = 1
    max_cnt = 1
    while q:
        x, y = q.popleft()
        # print(f"x, y = {x, y}")
        # print(f"graph = {graph[x][y]}")
        binary_num = bin(graph[x][y])[2:].zfill(4)
        # print(f"binary_num = {binary_num}")
        for i in range(4):
            nx, ny = dx[i] + x, dy[i] + y
            # print(f"nx, ny = {nx, ny}")
            if binary_num[i] == '0':  # 남 동 북 서 경우 뚫려있는 경우 bfs 진행
                if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                    visited[nx][ny] = 1
                    q.append([nx, ny])
                    max_cnt += 1
    return max_cnt

# 방의 개수
cnt_room = 0

# 개수 카운트
for i in range(m):
    for j in range(n):
        if not visited[i][j]:
            # print("==========================================")
            # print(f"i,j = {i, j}")
            cnt_room += 1
            max_room = max(max_room, bfs(i, j))
print("00000000000000000000000000000000000000000")
# 벽을 제거하면서 이동함
max_remove_wall = 0
for i in range(m):
    for j in range(n):
        for k in [1, 2, 4, 8]:
            visited = [[0] * n for _ in range(m)]
            # print(f"k = {k}")
            # print("==========================================")
            if graph[i][j] - k < 0:
                # print("88888888888888888888")
                # print(f"i,j = {i, j}")
                # print("88888888888888888888")
                continue
            # print(f"i,j = {i, j}")
            graph[i][j] -= k
            # print(f"graph = {graph}")
            max_remove_wall = max(max_remove_wall, bfs(i, j))
            graph[i][j] += k

print(cnt_room)
print(max_room)
print(max_remove_wall)
