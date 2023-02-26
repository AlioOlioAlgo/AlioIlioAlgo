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

input = sys.stdin.readline

R, C = map(int, input().split())
board = [list(input().rstrip()) for _ in range(R)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
cnt = 1

def bfs(x, y):
    queue = set([(x, y, board[x][y])])
    global cnt
    while queue:
        x, y, b = queue.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < R and 0 <= ny < C and board[nx][ny] not in b:
                queue.add((nx, ny, b + board[nx][ny]))
                cnt = max(cnt, len(b) + 1)

bfs(0, 0)
print(cnt)
