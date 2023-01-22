"""
 *packageName    :
 * fileName       : 숫자의 순차적 이동
 * author         : ipeac
 * date           : 2023-01-21
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2023-01-21        ipeac       최초 생성
 """
import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
graph = [
    list(map(int, sys.stdin.readline().split()))
    for _ in range(n)
]
# print(f"graph = {graph}")

dx = [0, 0, 1, 1, 1, -1, -1, -1]
dy = [1, -1, 1, 0, -1, 1, 0, -1]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def find_number(integer):
    for i in range(n):
        for j in range(n):
            if graph[i][j] == integer:
                return i, j

def simulate():
    for i in range(1, (n * n) + 1):
        x, y, = find_number(i)
        max_value = 0
        max_x, max_y = x, y
        for k in range(8):
            nx, ny = x + dx[k], y + dy[k]
            if not in_range(nx, ny):
                continue
            if max_value < graph[nx][ny]:
                max_value = graph[nx][ny]
                max_x, max_y = nx, ny
        graph[x][y], graph[max_x][max_y] = graph[max_x][max_y], graph[x][y]  # 자리 교체

for _ in range(m):
    simulate()

for num in graph:
    print(*num)
