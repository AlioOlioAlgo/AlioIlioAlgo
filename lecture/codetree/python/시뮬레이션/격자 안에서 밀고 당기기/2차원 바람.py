"""
 *packageName    :
 * fileName       : 2차원 바람
 * author         : ipeac
 * date           : 2022-12-31
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-12-31        ipeac       최초 생성
 """
import math

n, m, q = map(int, input().split())
graph = [
    list(map(int, input().split()))
    for _ in range(n)
]

print(f"graph = {graph}")
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def return_avg(i, j):
    sum = 0
    cnt = 0
    for k in range(4):
        nx, ny = i + dx[k], j + dy[k],
        if 0 <= nx < n and 0 <= ny < m:
            cnt += 1
            sum += graph[nx][ny]
    return sum, cnt

tmp_graph = [num[:] for num in graph]

for _ in range(q):
    graph = [num[:] for num in tmp_graph]
    # print(f"tmp_graph = {tmp_graph}")
    # print("==========================================")
    r1, c1, r2, c2 = map(int, input().split())
    print(f"r1,c1,r2,c2 = {r1, c1, r2, c2}")
    
    # print("==========================================")
    # 가로 돌리기
    for index in range(c2 - 1, c1 - 1, -1):
        # print(f"index = {index}")
        graph[r1 - 1][index] = graph[r1 - 1][index - 1]
    graph[r1 - 1][c1 - 1] = tmp_graph[r1][c1 - 1]  # 첫 값 이전값으로 채우기
    # print("==========================================")
    # 오른쪽 세로 돌리기
    for index in range(r2 - 1, r1, -1):
        # print(f"index = {index}")
        graph[index][c2 - 1] = graph[index - 1][c2 - 1]
    graph[r1][c2 - 1] = tmp_graph[r1 - 1][c2 - 1]
    # print("==========================================")
    # 가로 반대로 돌리기 (아래)
    for index in range(c1 - 1, c2 - 1):
        # print(f"index = {index}")
        graph[r2 - 1][index] = graph[r2 - 1][index + 1]
    graph[r2 - 1][c2 - 2] = tmp_graph[r2 - 1][c2 - 1]
    
    # print("==========================================")
    # 세로 왼쪽 돌리기
    for index in range(r1 - 1, r2 - 1):
        # print(f"index = {index}")
        graph[index][c1 - 1] = graph[index + 1][c1 - 1]
    graph[r2 - 2][c1 - 1] = tmp_graph[r2 - 1][c1 - 1]
    
    # pprint.pprint(graph, width=50)
    # 하나씩 근처 평균값으로 치환해주기
    for i in range(r1 - 1, r2):
        for j in range(c1 - 1, c2):
            sum_value, cnt_value = return_avg(i, j)
            tmp_graph[i][j] = math.floor((sum_value + graph[i][j]) / (cnt_value + 1))
for line in tmp_graph:
    print(*line)
