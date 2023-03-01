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

input = sys.stdin.readline

graph = [
    [
        list(map(int, input().rstrip().split()))
        for _ in range(5)
    ] for _ in range(5)
]

def in_range(x, y, z):
    return 0 <= x < 5 and 0 <= y < 5 and 0 <= z < 5

def bfs(maze):
    move = ((0, 0, 1), (0, 0, -1), (1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0))
    if maze[0][0][0] == 0 or maze[-1][-1][-1] == 0:
        return -1
    q = deque()
    visited = set()
    visited.add((0, 0, 0))
    q.append((0, 0, 0, 0))
    while q:
        x, y, z, cnt = q.popleft()
        for i in range(6):
            nx, ny, nz = x + move[i][0], y + move[i][1], z + move[i][2]
            if in_range(nx, ny, nz) and (nx, ny, nz) not in visited and maze[nx][ny][nz] == 1:
                q.append((nx, ny, nz, cnt + 1))
                visited.add((nx, ny, nz))
                if (nx, ny, nz) == (4, 4, 4):
                    return cnt + 1
    return -1

ans = -1
for combi in permutations(range(5)):
    maze = []
    for value in combi:
        maze.append(graph[value])
    for rotate1 in range(4):
        maze[0] = list(map(list, zip(*maze[0][::-1])))  # 각 층을 90도 회전한 값..
        for rotate2 in range(4):
            maze[1] = list(map(list, zip(*maze[1][::-1])))  # 각 층을 90도 회전한 값..
            for rotate3 in range(4):
                maze[2] = list(map(list, zip(*maze[2][::-1])))  # 각 층을 90도 회전한 값..
                for rotate4 in range(4):
                    maze[3] = list(map(list, zip(*maze[3][::-1])))  # 각 층을 90도 회전한 값..
                    for rotate5 in range(4):
                        maze[4] = list(map(list, zip(*maze[4][::-1])))
                        result = bfs(maze)
                        if result != -1:
                            if ans == 12:
                                print(12)
                                sys.exit(0)
                            
                            if ans == -1:
                                ans = result
                            else:
                                ans = min(ans, result)
print(ans)
