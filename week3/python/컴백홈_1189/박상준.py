"""
 *packageName    : 
 * fileName       : 박상준
 * author         : ipeac
 * date           : 2022-10-31
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-10-31        ipeac       최초 생성
 """
r, c, k = map(int, input().split())
graph = [
    list(map(str, input()))
    for _ in range(r)
]
# print(f"r,c,k = {r, c, k}")
# print(f"graph = {graph}")
# r, c, k = (3, 4, 6)
# graph = [['.', '.', '.', '.'], ['.', 'T', '.', '.'], ['.', '.', '.', '.']]
visited = [[0] * c for _ in range(r)]
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
ans = []

def dfs(i, j, visited, cnt):
    if i == 0 and j == c - 1:
        ans.append(cnt)
        return
    for xx, yy in zip(dx, dy):
        nx, ny = xx + i, yy + j
        if 0 <= nx < r and 0 <= ny < c and not visited[nx][ny] and graph[nx][ny] != 'T':
            visited[nx][ny] = 1
            dfs(nx, ny, visited, cnt + 1)
            visited[nx][ny] = 0

visited[r - 1][0] = 1
dfs(r - 1, 0, visited, 1)
print(ans.count(k))
