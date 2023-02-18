"""
 *packageName    : 
 * fileName       : 20230218
 * author         : ipeac
 * date           : 2023-02-18
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2023-02-18        ipeac       최초 생성
"""
r, c, k = map(int, input().split())
ans = 0
graph = [
    list(map(str, input()))
    for _ in range(r)
]

dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]

visited = [
    [False for _ in range(c)]
    for _ in range(r)
]
print(f"graph  ==> {graph}")

def in_range(x, y):
    return 0 <= x < r and 0 <= y < c

def can_go(x, y):
    if graph[x][y] == "T":
        return False
    return True

def dfs(x, y, cnt):
    global ans
    if x == 0 and y == c - 1:
        if cnt == k:
            ans += 1
        return
    
    visited[x][y] = True
    for xx, yy in zip(dx, dy):
        nx, ny = xx + x, yy + y
        if in_range(nx, ny) and can_go(nx, ny) and not visited[nx][ny]:
            visited[nx][ny] = True
            dfs(nx, ny, cnt + 1)
            visited[nx][ny] = False

dfs(r - 1, 0, 1)
print(ans)
