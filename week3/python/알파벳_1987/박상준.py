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
import sys

sys.setrecursionlimit(10 ** 4)

r, c = map(int, sys.stdin.readline().split())
graph = [
    list(map(lambda x: ord(x) - 65, sys.stdin.readline()))
    for _ in range(r)
]
#
# print(f"r,c = {r, c}")
# print(f"graph = {graph}")
# r, c = (2, 4)
# graph = [['C', 'A', 'A', 'B'], ['A', 'D', 'C', 'B']]
list_alpha = [0 for _ in range(26)]
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
max_cnt = 0

def dfs(i, j, cnt):
    global max_cnt
    max_cnt = max(cnt, max_cnt)
    
    for k in range(4):
        nx, ny = dx[k] + i, dy[k] + j
        # list_alpha 가 0 이라면 아직 기입되지 않은 거임 ㅇㅇ
        if 0 <= nx < r and 0 <= ny < c and list_alpha[graph[nx][ny]] == 0:
            list_alpha[graph[nx][ny]] = 1
            dfs(nx, ny, cnt + 1)
            list_alpha[graph[nx][ny]] = 0  # 백트래킹

list_alpha[graph[0][0]] = 1
dfs(0, 0, 1)
print(max_cnt)
