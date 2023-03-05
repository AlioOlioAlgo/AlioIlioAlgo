"""
 *packageName    : 
 * fileName       : 1941.소문난 칠공주
 * author         : ipeac
 * date           : 2023-03-04
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2023-03-04        ipeac       최초 생성
"""
from collections import deque
from itertools import combinations

graph = [
    list(map(str, input()))
    for _ in range(5)
]
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]

def in_range(x, y):
    return 0 <= x < 5 and 0 <= y < 5

def connected(combi):
    x, y = combi[0] // 5, combi[0] % 5
    visited = [
        [False for _ in range(5)]
        for _ in range(5)
    ]
    visited[x][y] = True
    
    q = deque()
    q.append((x, y))
    
    cnt = 1
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if in_range(nx, ny) and (nx * 5 + ny) in combi and not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((nx, ny))
                cnt += 1
    
    return cnt

ans = 0
for combi in combinations(range(25), 7):
    if sum(graph[i // 5][i % 5] == 'S' for i in combi) >= 4:  # 이다솜파가 4명이상이여합니다.
        # 연결되어있는지 확인합니다.
        if connected(combi) == 7:
            ans += 1

print(ans)
