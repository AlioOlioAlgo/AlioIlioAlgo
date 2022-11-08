"""
 *packageName    :
 * fileName       : 박상준
 * author         : ipeac
 * date           : 2022-11-07
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-11-07        ipeac       최초 생성
 """
# r, c = 2, 4  # 세로 가로
# graph = [['C', 'A', 'A', 'B'], ['A', 'D', 'C', 'B']]
r, c = map(int, input().split())
graph = [list(map(str, input())) for _ in range(r)]
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
visited = [[0] * c for _ in range(r)]
ans = []
max_cnt = 0

# 1행 1열에 말이 있음 (0,0) 부터 시작
def dfs(row, col, cnt, result):
    global max_cnt
    max_cnt = max(cnt, max_cnt)
    for xx, yy, in zip(dx, dy):
        nx, ny = xx + row, yy + col
        if 0 <= nx < r and 0 <= ny < c and graph[nx][ny] not in result:
            result.append(graph[nx][ny])
            dfs(nx, ny, cnt + 1, ans)
            result.pop()

ans.append(graph[0][0])
dfs(0, 0, 1, ans)
print(max_cnt)
