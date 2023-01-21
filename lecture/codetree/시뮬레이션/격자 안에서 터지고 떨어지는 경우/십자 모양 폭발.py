"""
 *packageName    :
 * fileName       : 십자 모양 폭발
 * author         : ipeac
 * date           : 2023-01-01
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2023-01-01        ipeac       최초 생성
 """
import pprint

n = int(input())
graph = [
    list(map(int, input().split()))
    for _ in range(n)
]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

boom_x, boom_y = map(int, input().split())
boom_x, boom_y = boom_x - 1, boom_y - 1

target_number = graph[boom_x][boom_y]
print(f"target_number = {target_number}")
graph[boom_x][boom_y] = 0
for i in range(4):
    x, y = boom_x, boom_y
    for j in range(target_number - 1):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            graph[nx][ny] = 0
        else:
            break
        x, y = nx, ny
# print(f"graph = {graph}")
# 세로 1 ~ 끝까지 밑으로 당겨준다.
pprint.pprint(graph, width=50)
tmp_graph = [[0 for _ in range(n)] for _ in range(n)]

for col in range(n):
    print("==========================================")
    cursor = n - 1
    for row in range(n - 1, -1, -1):
        if graph[row][col] != 0:
            tmp_graph[cursor][col] = graph[row][col]
            cursor -= 1
    pprint.pprint(tmp_graph, width=50)
for num in tmp_graph:
    print(*num)
