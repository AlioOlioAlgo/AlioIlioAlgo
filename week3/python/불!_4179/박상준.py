"""
 *packageName    : 
 * fileName       : 박상준
 * author         : ipeac
 * date           : 2022-10-29
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-10-29        ipeac       최초 생성
 """
from collections import deque

r, c = map(int, input().split())
miro = [
    list(map(str, input()))
    for _ in range(r)
]
# print(f"r,c = {r, c}")
# print(f"miro = {miro}")

dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]

# r, c = (4, 4)
# miro = [['#', '#', '#', '#'], ['#', 'J', 'F', '#'], ['#', '.', '.', '#'], ['#', '.', '.', '#']]

fire_queue = deque()
jihun_queue = deque()

visited_f = [[0] * c for _ in range(r)]
visited_j = [[0] * c for _ in range(r)]

for i in range(r):
    for j in range(c):
        if miro[i][j] == 'F':
            fire_queue.append([i, j])
            visited_f[i][j] = 1
        
        elif miro[i][j] == 'J':
            jihun_queue.append([i, j])
            visited_j[i][j] = 1

def bfs():
    while fire_queue:
        x, y = fire_queue.popleft()
        for xx, yy in zip(dx, dy):
            nx, ny, = xx + x, yy + y
            if 0 <= nx < r and 0 <= ny < c and not visited_f[nx][ny] and miro[nx][ny] != '#':
                fire_queue.append([nx, ny])
                visited_f[nx][ny] = visited_f[x][y] + 1
    # print(f"visited_f = {visited_f}")
    while jihun_queue:
        x, y = jihun_queue.popleft()
        for xx, yy in zip(dx, dy):
            nx, ny = xx + x, yy + y
            if 0 <= nx < r and 0 <= ny < c:
                if not visited_j[nx][ny] and miro[nx][ny] != '#' and (visited_j[x][y] + 1 < visited_f[nx][ny] or not visited_f[nx][ny]):
                    jihun_queue.append([nx, ny])
                    visited_j[nx][ny] = visited_j[x][y] + 1
            # 그래프 밖으로 꾸역꾸역 기어나가는 경우 > 위험에서 벗어난거임
            else:
                return visited_j[x][y]
    return "IMPOSSIBLE"

print(bfs())
