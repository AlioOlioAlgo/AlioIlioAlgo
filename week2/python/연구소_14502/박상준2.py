"""
 *packageName    :
 * fileName       : 박상준2
 * author         : ipeac
 * date           : 2022-10-29
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-10-29        ipeac       최초 생성
 """

import copy
from collections import deque

# n, m = map(int, input().split())
# graph = [
#     list(map(int, input().split()))
#     for _ in range(n)
# ]
# print(f"n,m = {n, m}")
# print(f"graph = {graph}")

n, m = (4, 6)
graph = [[0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 2], [1, 1, 1, 0, 0, 2], [0, 0, 0, 0, 0, 2]]
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
max_value = 0

def bfs():
    global max_value  # 정답을 기록할 수있는 변수
    
    cnt = 0
    # 큐 형식
    # deque는 스택과 큐의 기능을 모두 가진 객체로 출입구를 양쪽에 가지고 있다.
    # 스택처럼써도 되고, 큐처럼 써도 된다. -> 입출력도 배열보다 효과적
    q = deque()
    # 2차원 배열은 파이썬의 경우 깊은 복사가 deepcopy 로 밖에 안되는듯;
    # 기존  graph 참조하지 않도록 별도의 그래프를 깊은 복사 처리
    tmp_graph = copy.deepcopy(graph)
    # 모든 2 의 위치를 담는다
    for i in range(n):
        for j in range(m):
            if tmp_graph[i][j] == 2:
                q.append([i, j])  # (0,2)
    # 2 확산을 위해서 visited 설정
    visited = [[0] * m for _ in range(n)]
    
    while q:
        x, y = q.popleft()  # (0,2)     # (1,2)
        for xx, yy, in zip(dx, dy):  # 바이러스는 상하 좌우로 이동
            nx, ny = xx + x, yy + y
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and graph[nx][ny] == 0:
                tmp_graph[nx][ny] = 2
                visited[nx][ny] = 1
                q.append([nx, ny])  # (1,2)
    for i in range(n):
        cnt += tmp_graph[i].count(0)
    
    max_value = max(max_value, cnt)

# cnt =3 이 될때까지 벽을 재귀적으로 만든다. 결국 0에 해당 하는 모든 graph 에 벽이 세워질 것이며 모든 경우의 수가 대비될 것이다.
def make_wall(start_row, start_col, cnt):
    if cnt == 3:
        bfs()
        return
    # 이전 벽을 세운 위치보다 col + 1 위치에 세워지게 된다.
    for i in range(start_row, n):
        for j in range(start_col, m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                make_wall(i, j + 1, cnt + 1)
                graph[i][j] = 0
        start_col = 0  # 스타트 col 을 0으로 설정한다. 0 1 0 2 0 3 ... 돌다가 마지막 col을 만나면 0 으로 초기화 -> row +1 순차적으로 2차원 배열을 탐색한다.

make_wall(0, 0, 0)
print(max_value)
