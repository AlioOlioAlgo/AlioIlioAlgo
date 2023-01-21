"""
 *packageName    :
 * fileName       : 숫자가 가장 큰 인접한 곳으로 동시에 이동
 * author         : ipeac
 * date           : 2023-01-21
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2023-01-21        ipeac       최초 생성
 """
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
n, m, t = map(int, input().split())
graph = [
    list(map(int, input().split()))
    for _ in range(n)
]
now_ball = [
    [0 for _ in range(n)]
    for _ in range(n)
]

# 구슬의 위치
for _ in range(m):
    x, y = map(int, input().split())
    now_ball[x - 1][y - 1] += 1
print(f"now_ball = {now_ball}")

def simulate():
    next_ball = [
        [0 for _ in range(n)]
        for _ in range(n)
    ]
    
    for i in range(n):
        for j in range(n):
            move_x, move_y = get_next_pos(i, j)  # 이동할 위치
            if move_x == 1 and move_y == 1:
                continue
            next_ball[move_x][move_y] += 1

# 해당 값이 격자 안에 들어가 있는지 체크한다.
def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

# 해당 구슬 위치에서 다음으로 갈 곳의 위치를 찾는다.
def get_next_pos(x, y):
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if graph[nx][ny] > graph[x][y]:  # 해당 값이 더 크다면 그쪽으로 이동시켜준다.
            return nx, ny
    return -1, -1

def dup_value_remove():
    for i in range(n):
        for j in range(n):
            if
    pass
