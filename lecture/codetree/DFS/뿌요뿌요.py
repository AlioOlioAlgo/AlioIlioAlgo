"""
 *packageName    : 
 * fileName       : 뿌요뿌요
 * author         : ipeac
 * date           : 2023-02-16
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2023-02-16        ipeac       최초 생성
"""
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

n = int(input())
graph = [
    list(map(int, input().split()))
    for _ in range(n)
]
visited = [
    [False for _ in range(n)]
    for _ in range(n)
]
cnt = 0

save_block = []

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def dfs(x, y, value):
    global block
    for xx, yy in zip(dx, dy):
        nx, ny = xx + x, yy + y
        if in_range(nx, ny) and not visited[nx][ny] and graph[nx][ny] == value:
            block += 1
            visited[nx][ny] = True
            dfs(nx, ny, value)

for i in range(n):
    for j in range(n):
        block = 0
        if not visited[i][j]:
            visited[i][j] = True
            block += 1
            dfs(i, j, graph[i][j])
            save_block.append(block)
            if block >= 4:
                cnt += 1
print(cnt, max(save_block))
