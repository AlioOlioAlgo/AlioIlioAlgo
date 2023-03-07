"""
 *packageName    : 
 * fileName       : 2206.벽 부수고 이동하기
 * author         : ipeac
 * date           : 2023-03-07
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2023-03-07        ipeac       최초 생성
"""
from collections import deque

n, m = map(int, input().split())

graph = [
    list(map(int, input()))
    for _ in range(n)
]
print(f"graph  ==> {graph}")

def bfs():
    visited = [
        [False for _ in range(m)]
        for _ in range(n)
    ]
    visited[0][0] = True
    q = deque()
    q.append((0, 0))
    
    while q:
        x, y = q.popleft()

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            graph[i][j] = 0
            bfs()
            graph[i][j] = 1
