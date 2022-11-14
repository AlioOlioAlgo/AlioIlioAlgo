"""
 *packageName    :
 * fileName       : 박상준2
 * author         : ipeac
 * date           : 2022-11-04
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-11-04        ipeac       최초 생성
 """
import pprint
from collections import deque

dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
r, c = map(int, input().split())
miro = [
    list(map(str, input()))
    for _ in range(r)
]
# print(f"r,c = {r, c}")
# print(f"miro = {miro}")

# r, c = (4, 4)
# miro = [['#', '#', '#', '#'], ['#', 'J', 'F', '#'], ['#', '.', '.', '#'], ['#', '.', '.', '#']]

f_deque = deque()
j_deque = deque()

# 서로 다른 케이스라고 고려함
visited_f = [[0] * c for _ in range(r)]
visited_j = [[0] * c for _ in range(r)]

# 불과 지훈이 위치를 큐에 담아준다
# 파이썬 deque = 자바 queue + stack 개념
# 양 쪽 출입구가 열려있음 왼쪽 오른쪽 데이터 추가 혹은 Pop이 가능하다.
for i in range(r):
    for j in range(c):
        if miro[i][j] == 'F':
            f_deque.append([i, j])
            visited_f[i][j] = 1
        elif miro[i][j] == 'J':
            j_deque.append([i, j])
            visited_j[i][j] = 1

# @ 일단 불과 지훈의 위치 데이터와 해당 위치에 visited 타임을 각각 1로 설정함

def bfs():
    # 불 4방향 댄스
    # 불은 4방향으로 움직이는 대신
    # 0 <= nx < r and 0 <= ny < c -> 배열 밖으로 나가지 않으며
    # visited_f[nx][ny] and miro[nx][ny] != '#' -> bfs도는 방향에 불이 방문했으면 안됨 + 미로가 벽이 아니다.
    # 이후 bfs진행
    #  visited_f[nx][ny] = visited_f[x][y] + 1  # 각 visited 마다 움직인 time 을 기록
    # 최종 진행 결과
    #     # [[0, 0, 0, 0],#불이 방문한 시점을 기록한 visited_f
    #     #  [0, 2, 1, 0],
    #     #  [0, 3, 2, 0],
    #     #  [0, 4, 3, 0]]
    #     #
    while f_deque:
        x, y = f_deque.popleft()
        for xx, yy in zip(dx, dy):
            nx, ny = xx + x, yy + y
            if 0 <= nx < r and 0 <= ny < c and not visited_f[nx][ny] and miro[nx][ny] != '#':
                visited_f[nx][ny] = visited_f[x][y] + 1  # 각 visited 마다 움직인 time 을 기록
                f_deque.append([nx, ny])
    pprint.pprint(visited_f, width=50)
    
    # 기본적으로 배열의 밖으로 나가는 경우 && 나가지 않는 경우로 나눔
    # 나가는 경우 ->(nx,ny)가 미로 탈출이라 원점 (x,y) 값이 최단 탈출이 된다.
    # 나가지 않고 미로 안에 있는 경우 -> 0 <= nx < r and 0 <= ny < c:
    #
    # not visited_j[nx][ny] and miro[nx][ny] != '#' -> 지훈이 방문하지 않고 미로가 벽이 아닌 경우
    # (visited_j[x][y] + 1 < visited_f[nx][ny] or not visited_f[nx][ny]) -> 지훈의 현재 위치의 +1 한 값이 이동한 구간의 불의 이동 시점보다 이전이라면
    # 지훈이 이동가능하다는 말이 된다. |||| 또한 불이 오지 못한 곳이라면 지훈이 이동가능함
    #
    # 최종 지훈의 방문 시점을 기록한 visited_j
    # [[0, 0, 0, 0],
    #  [0, 1, 0, 0],
    #  [0, 2, 0, 0],
    #  [0, 3, 0, 0]]
    #
    # 지훈이 움직인 방향
    while j_deque:
        x, y = j_deque.popleft()
        for xx, yy in zip(dx, dy):
            nx, ny = xx + x, yy + y
            
            if 0 <= nx < r and 0 <= ny < c:
                if not visited_j[nx][ny] and miro[nx][ny] != '#' and (visited_j[x][y] + 1 < visited_f[nx][ny] or not visited_f[nx][ny]):
                    visited_j[nx][ny] = visited_j[x][y] + 1
                    j_deque.append([nx, ny])
            else:
                pprint.pprint(visited_j, width=50)
                return visited_j[x][y]
    return "IMPOSSIBLE"

print(bfs())
