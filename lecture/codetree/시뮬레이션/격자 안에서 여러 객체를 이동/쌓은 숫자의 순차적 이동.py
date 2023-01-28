"""
 *packageName    :
 * fileName       : 쌓은 숫자의 순차적 이동
 * author         : ipeac
 * date           : 2023-01-23
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2023-01-23        ipeac       최초 생성
 """
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [
    [[] for _ in range(n)]
    for _ in range(n)
]
for i in range(n):
    line_value = list(map(int, input().split()))
    for j in range(n):
        graph[i][j].append(line_value[j])

print(f"graph = {graph}")
move_ball = list(map(int, input().split()))

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def find_number(num):
    for i in range(n):
        for j in range(n):
            for k in range(len(graph[i][j])):
                if graph[i][j][k] == num:
                    return i, j, k

def find_max_value_and_change_max_value(x, y, inner_idx):
    print(f"x,y,inner_idx = {x, y, inner_idx}")
    max_value = 0
    max_x, max_y = x, y
    for k in range(8):
        nx, ny = x + dx[k], y + dy[k]
        if not in_range(nx, ny) or len(graph[nx][ny]) == 0:
            continue
        # print(f"graph[nx][ny] = {graph[nx][ny]}")
        max_temp = max(graph[nx][ny])
        
        if max_value < max_temp:
            max_value = max_temp
            max_x, max_y = nx, ny
    
    if max_value != 0:
        print(f"graph[x][y] = {graph[x][y]}")
        print(f"graph[max_x][max_y] = {graph[max_x][max_y]}")
        tmp = graph[x][y][:inner_idx + 1] + graph[max_x][max_y]
        graph[max_x][max_y] = tmp
        graph[x][y] = graph[x][y][inner_idx + 1:]

for move in move_ball:
    find_x, find_y, inner_idx = find_number(move)
    find_max_value_and_change_max_value(find_x, find_y, inner_idx)

for num in graph:
    for num2 in num:
        if len(num2) == 0:
            print('None')
        else:
            print(*num2)
