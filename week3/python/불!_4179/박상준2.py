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

for i in range(r):
    for j in range(c):
        if miro[i][j] == 'F':
            f_deque.append([i, j])
            visited_f[i][j] = 1
        elif miro[i][j] == 'J':
            j_deque.append([i, j])
            visited_j[i][j] = 1

def bfs():
    # 불 4방향 댄스
    while f_deque:
        x, y = f_deque.popleft()
        for xx, yy in zip(dx, dy):
            nx, ny = xx + x, yy + y
            if 0 <= nx < r and 0 <= ny < c and not visited_f[nx][ny] and miro[nx][ny] != '#':
                visited_f[nx][ny] = visited_f[x][y] + 1  # 각 visited 마다 움직인 time 을 기록
                f_deque.append([nx, ny])
    # pprint.pprint(visited_f, width=50)
    # 지훈이 움직인 방향
    while j_deque:
        x, y = j_deque.popleft()
        for xx, yy in zip(dx, dy):
            nx, ny = xx + x, yy + y
            if 0 <= nx < r and 0 <= ny < c:
                # 불이 난 지점보다
                if not visited_j[nx][ny] and miro[nx][ny] != '#' and (visited_j[x][y] + 1 < visited_f[nx][ny] or not visited_f[nx][ny]):
                    visited_j[nx][ny] = visited_j[x][y] + 1
                    j_deque.append([nx, ny])
            else:
                return visited_j[x][y]
    return "IMPOSSIBLE"
    # pprint.pprint(visited_j, width=50)

print(bfs())
