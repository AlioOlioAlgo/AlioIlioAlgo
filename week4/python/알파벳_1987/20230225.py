"""
 *packageName    : 
 * fileName       : 20230225
 * author         : ipeac
 * date           : 2023-02-25
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2023-02-25        ipeac       최초 생성
"""
import sys

sys.setrecursionlimit(10 ** 4)

r, c, = map(int, input().rstrip().split())
dx, dy = [0, 0, -1, 1], [1, -1, 0, 0]
graph = [
    list(map(lambda x: ord(x) - 65, sys.stdin.readline().rstrip()))
    for _ in range(r)
]
dic = [0 for i in range(0, 26)]

def in_range(x, y):
    return 0 <= x < r and 0 <= y < c

ans = -1e9

def dfs(x, y, in_ans):
    global ans
    if ans < in_ans:
        ans = max(ans, in_ans)
    
    for i in range(4):
        nx, ny = dx[i] + x, dy[i] + y
        if in_range(nx, ny) and dic[graph[nx][ny]] == 0:
            dic[graph[nx][ny]] = 1
            dfs(nx, ny, in_ans + 1)
            dic[graph[nx][ny]] = 0

dic[graph[0][0]] = 1
dfs(0, 0, 1)
print(ans)
