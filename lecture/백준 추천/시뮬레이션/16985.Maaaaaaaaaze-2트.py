"""
 *packageName    : 
 * fileName       : 16985.Maaaaaaaaaze
 * author         : ipeac
 * date           : 2023-03-01
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2023-03-01        ipeac       최초 생성
"""
import sys
from collections import deque
from itertools import permutations

graph = [
    [
        list(map(int, input().split()))
        for _ in range(5)
    ]
    for _ in range(5)
]
move = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, -1), (0, 0, 1))  # 남 북 동 서 상 하

def in_range(x, y, z):
    return 0 <= x < 5 and 0 <= y < 5 and 0 <= z < 5

def bfs(maze):
    visited = [
        [
            [False for _ in range(5)]
            for _ in range(5)
        ]
        for _ in range(5)
    ]
    q = deque()
    q.append((0, 0, 0, 0))
    visited[0][0][0] = True
    while q:
        x, y, z, cnt = q.popleft()
        if (x, y, z) == (4, 4, 4):
            return cnt

        for xx, yy, zz in move:
            nx, ny, nz = x + xx, y + yy, z + zz
            if in_range(nx, ny, nz) and not visited[nx][ny][nz] and maze[nx][ny][nz]:
                q.append((nx, ny, nz, cnt + 1))
                visited[nx][ny][nz] = True
    return 1e9

ans = 1e9

for combi in permutations(range(5)):  # maze 에 몇번째의 층을 기입할 것 인지 체크합니다.
    maze = []
    for num in combi:
        maze.append(graph[num])
    # 오리지널 메이즈
    # original_maze = [num[:] for num in maze]
    # 만들어진 maze 를 기준으로  1층 2층 3층 4층 5층을 각각 4번 돌린 maze 를 만들어냅니다.
    for rotate1 in range(4):
        maze[0] = list(map(list, zip(*maze[0][::-1])))  # 시계방향으로 90도 돌립니다.
        for rotate2 in range(4):
            maze[1] = list(map(list, zip(*maze[1][::-1])))  # 시계 방향으로 90도 돌립니다.
            for rotate3 in range(4):
                maze[2] = list(map(list, zip(*maze[2][::-1])))
                for rotate4 in range(4):
                    maze[3] = list(map(list, zip(*maze[3][::-1])))
                    for rotate5 in range(4):
                        maze[4] = list(map(list, zip(*maze[4][::-1])))
                        if maze[0][0][0] == 0:
                            continue
                        # maze 완성 모든 케이스 고려합니다.
                        value = bfs(maze)
                        ans = min(ans, value)
                        if ans == 12:
                            print(12)
                            sys.exit(0)

print(-1) if ans == 1e9 else print(ans)
