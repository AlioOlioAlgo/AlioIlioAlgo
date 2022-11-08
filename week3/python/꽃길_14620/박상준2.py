"""
 *packageName    :
 * fileName       : 박상준2
 * author         : ipeac
 * date           : 2022-11-08
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-11-08        ipeac       최초 생성
 """
import sys

sys.setrecursionlimit(10 ** 8)
n = int(input())

flower = [list(map(int, input().split())) for _ in range(n)]
# print(f"flower = {flower}")
# flower = [[1, 0, 2, 3, 3, 4], [1, 1, 1, 1, 1, 1], [0, 0, 1, 1, 1, 1], [3, 9, 9, 0, 1, 99], [9, 11, 3, 1, 0, 3], [12, 3, 0, 0, 0, 1]]
visited = [[0] * n for _ in range(n)]
dx, dy = [0, 0, 0, 1, -1], [0, 1, -1, 0, 0],
min_value = sys.maxsize
total = 0

def check(i, j):
    for xx, yy in zip(dx, dy):
        nx, ny = xx + i, yy + j
        if visited[nx][ny]:
            return False
    return True

def dfs(cnt):
    global min_value, total
    if cnt == 3:
        min_value = min(min_value, total)
        return
    for i in range(1, n - 1):
        for j in range(1, n - 1):
            if check(i, j):  # 5방향 체크
                for xx, yy in zip(dx, dy):
                    nx, ny = xx + i, yy + j
                    visited[nx][ny] = 1
                    total += flower[nx][ny]
                    # 5방향의 땅값을 저장
                dfs(cnt + 1)
                
                for xx, yy in zip(dx, dy):
                    nx, ny = xx + i, yy + j
                    visited[nx][ny] = 0
                    total -= flower[nx][ny]

dfs(0)
print(min_value)
