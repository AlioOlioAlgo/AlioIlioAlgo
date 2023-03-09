"""
 *packageName    : 
 * fileName       : 2146.다리 만들기
 * author         : ipeac
 * date           : 2023-03-09
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2023-03-09        ipeac       최초 생성
"""
import sys
from collections import deque

n = int(input())
graph = [
    list(map(int, input().split()))
    for _ in range(n)
]
# print(f"graph  ==> {graph}")

dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]

edges = []
visited = [
    [-1 for _ in range(n)]
    for _ in range(n)
]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

cnt = 0

def island_check(i, j, cnt):
    q = deque()
    q.append((i, j))
    visited[i][j] = cnt
    
    while q:
        x, y, = q.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if in_range(nx, ny):
                if graph[nx][ny] == 1 and visited[nx][ny] == -1:
                    q.append((nx, ny))
                    visited[nx][ny] = cnt

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and visited[i][j] == -1:
            island_check(i, j, cnt)
            cnt += 1

ans = sys.maxsize

def find_way(v):
    q = deque()
    dist = [
        [-1 for _ in range(n)]
        for _ in range(n)
    ]
    for i in range(n):
        for j in range(n):
            if visited[i][j] == v:
                dist[i][j] = 0
                q.append((i, j))
    # print("==========================visitied============================")
    # pprint.pprint(visited)
    # print("========================dist==============================")
    # pprint.pprint(dist)
    # print("=========================graph=============================")
    # pprint.pprint(graph)
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if in_range(nx, ny):
                # 다른 섬을 만난다.
                if graph[nx][ny] and visited[nx][ny] != v and visited[nx][ny] != -1:
                    # print("========================dist output==============================")
                    # print(f"dist[x][y]  ==> {dist[x][y]}")
                    # pprint.pprint(dist)
                    
                    return dist[x][y]
                # 바다며 다리 없음
                elif not graph[nx][ny] and dist[nx][ny] == -1:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))
    return 1e9

for v in range(cnt):
    ans = min(ans, find_way(v))
print(ans)
