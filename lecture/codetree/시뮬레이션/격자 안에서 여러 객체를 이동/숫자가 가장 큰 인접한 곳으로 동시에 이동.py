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
import sys

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

input = sys.stdin.readline
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

def simulate():
    global now_ball
    next_ball = [
        [0 for _ in range(n)]
        for _ in range(n)
    ]
    
    for i in range(n):
        for j in range(n):
            if now_ball[i][j]:  # now_ball 에 기록된 경우
                move_x, move_y = get_next_pos(i, j)  # 이동할 위치
                next_ball[move_x][move_y] += 1
    now_ball = dup_value_remove(next_ball)  # 중복값 제거하여 now_ball 에 저장해놓기

# 해당 값이 격자 안에 들어가 있는지 체크한다.
def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

# 해당 구슬 위치에서 다음으로 갈 곳의 위치를 찾는다.
def get_next_pos(x, y):
    max_value = 0
    max_pos_x, max_pos_y = x, y
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if not in_range(nx, ny):  # 격자 안에 있어야함 ㅇㅇ
            continue
        if graph[nx][ny] > max_value:  # 해당 값이 더 크다면 그쪽으로 이동시켜준다.
            max_value = graph[nx][ny]
            max_pos_x, max_pos_y, = nx, ny
    
    return max_pos_x, max_pos_y

# 2 이상으로 중복된 값 제거하기
def dup_value_remove(graph):
    for i in range(n):
        for j in range(n):
            if graph[i][j] >= 2:
                graph[i][j] = 0
    return graph

for _ in range(t):
    simulate()
ans = 0
for i in now_ball:
    ans += sum(i)
print(ans)
