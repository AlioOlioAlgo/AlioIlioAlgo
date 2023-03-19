"""
 *packageName    :
 * fileName       : 숫자가 더 큰 인접한 곳으로 이동
 * author         : ipeac
 * date           : 2023-01-11
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2023-01-11        ipeac       최초 생성
 """
n, r, c = map(int, input().split())
graph = [
    list(map(int, input().split()))
    for _ in range(n)
]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
now = graph[r - 1][c - 1]
x, y = r - 1, c - 1
print(now, end=" ")
while True:
    my_target = graph[x][y]
    for i in range(4):
        xx, yy = x + dx[i], y + dy[i]
        if 0 > xx or xx >= n or 0 > yy or yy >= n:
            continue
        target = graph[xx][yy]
        if target > my_target:
            my_target = target
            x, y = xx, yy
            print(target, end=" ")
            break
    else:
        break
