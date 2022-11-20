"""
 *packageName    :
 * fileName       : 박상준2
 * author         : ipeac
 * date           : 2022-11-19
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-11-19        ipeac       최초 생성
 """
import sys

dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]

sys.setrecursionlimit(10 ** 4)

r, c = map(int, input().split())  # 세로 r 가로 c
graph = [
    list(map(lambda x: ord(x) - 65, sys.stdin.readline()))  # 0 ~ 26 의 숫자로 기록한다.
    for _ in range(r)
]
max_cnt = -int(1e9)
alpha = [0 for i in range(26)]  # 26 개의 알파벳 기록 배열 ( 비트연산과 비슷함 )
alpha[graph[0][0]] = 1

# print(f"alpha = {alpha}")

def dfs(i, j, cnt):
    # print("start==========================================")
    # print(f"i,j = {i, j}")
    global max_cnt
    if cnt > max_cnt:
        max_cnt = cnt
    
    for k in range(4):
        nx, ny = dx[k] + i, dy[k] + j
        if 0 <= nx < r and 0 <= ny < c:
            # print(f"graph = {graph[nx][ny]}")
            if not alpha[graph[nx][ny]]:
                # print(f"tmp = {tmp}")
                # print(f"graph = {graph[nx][ny]}")
                alpha[graph[nx][ny]] = 1
                
                dfs(nx, ny, cnt + 1)
                alpha[graph[nx][ny]] = 0

dfs(0, 0, 1)
print(max_cnt)
