"""
 *packageName    :
 * fileName       : 트로미노
 * author         : ipeac
 * date           : 2022-12-28
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-12-28        ipeac       최초 생성
 """
n, m = map(int, input().split())
graph = [
    list(map(int, input().split()))
    for _ in range(n)
]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(i, j, plus):
    max_value = 0
    for s in range(4):
        index_x1, index_y1 = i + dx[s], j + dy[s]
        index_x2, index_y2 = i + dx[(s + plus) % 4], j + dy[(s + plus) % 4],
        if 0 <= index_x1 < n and 0 <= index_y1 < m and 0 <= index_x2 < n and 0 <= index_y2 < m:
            value = graph[index_x1][index_y1] + graph[index_x2][index_y2] + graph[i][j]
            max_value = max(max_value, value)
    return max_value

ans = 0
for i in range(n):
    for j in range(m):  # 격자 중앙점을 잡고 2개의 모양의 회전각을 잡는다. n^3
        ans = max(ans, bfs(i, j, 1))
        ans = max(ans, bfs(i, j, 2))
print(ans)
