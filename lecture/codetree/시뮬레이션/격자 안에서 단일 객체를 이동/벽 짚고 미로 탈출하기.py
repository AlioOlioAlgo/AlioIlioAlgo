"""
 *packageName    :
 * fileName       : 떨어지는 1자 블록
 * author         : ipeac
 * date           : 2023-01-11
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2023-01-11        ipeac       최초 생성
 """
import sys

n = int(input())
x, y = map(int, input().split())

graph = [
    list(input())
    for _ in range(n)
]

# print(f"graph = {graph}")

visited = [
    [0 for _ in range(n)]
    for _ in range(n)
]

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

# 동 북 서 남


def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def is_wall(x, y):
    return in_range(x, y) and graph[x][y] == '#'  # 벽이있고 그래프안에 없는 경우

way = 0
cnt = 0
x -= 1
y -= 1
while in_range(x, y):
    if visited[x][y]:
        print(-1)
        break
    visited[x][y] = 1
    next_x, next_y = x + dx[way], y + dy[way]
    
    if is_wall(next_x, next_y):  # 벽이 있고 그래프안에 있는 경우
        # 반시계방향으로 방향을 바꾼다.
        way += 1
        way %= 4
    elif not in_range(next_x, next_y):
        x, y = next_x, next_y
        cnt += 1
    else:
        rx, ry = next_x + dx[(way - 1) % 4], next_y + dy[(way - 1) % 4]  # 바로 오른쪽에 벽이 있는지 체크
        if is_wall(rx, ry):
            x, y = next_x, next_y
            cnt += 1
        else:
            x, y = rx, ry  # 2칸 이동후 90도로 꺾는다.
            way = (way - 1) % 4
            cnt += 2
else:  # 밖으로 나온경우
    print(cnt)
    sys.exit()
