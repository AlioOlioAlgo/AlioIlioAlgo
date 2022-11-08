"""
 *packageName    :
 * fileName       : 박상준2
 * author         : ipeac
 * date           : 2022-11-08
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-11-08        ipeac       최초 생성
 """
from collections import deque

n, m = map(int, input().split())
# 주난위치 x1,y1  ; 초코비 : x2,y2
x1, y1, x2, y2 = map(int, input().split())
# 4방향 순회
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
classroom = [list(map(str, input())) for _ in range(n)]
# print(f"classroom = {classroom}")
# classroom = [['#', '0', '0', '0', '0'], ['1', '1', '1', '1', '1'], ['0', '0', '0', '0', '*']]
# 움직인 횟수 기록용 dis
dis = [[-1] * m for _ in range(n)]

def bfs(i, j):
    q = deque()
    q.append([i, j])
    dis[i][j] = 0
    
    while q:
        # print(f"dis = {dis}")
        x, y = q.popleft()
        for xx, yy, in zip(dx, dy):
            nx, ny = xx + x, yy + y
            if 0 <= nx < n and 0 <= ny < m and dis[nx][ny] == -1:
                if classroom[nx][ny] == '#' or classroom[nx][ny] == '1':
                    dis[nx][ny] = dis[x][y] + 1
                    q.append([nx, ny])
                elif classroom[nx][ny] == '0':
                    dis[nx][ny] = dis[x][y]  # 같은 레벨임
                    q.appendleft([nx, ny])  # 같은 레벨은 먼저 큐에 담아서 연산해줘야함
    return dis[x2 - 1][y2 - 1]

# 주난의 위치부터 시작
print(bfs(x1 - 1, y1 - 1))
