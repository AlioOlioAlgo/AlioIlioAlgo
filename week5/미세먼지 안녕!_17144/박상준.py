"""
 *packageName    :
 * fileName       : 박상준
 * author         : ipeac
 * date           : 2022-11-24
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-11-24        ipeac       최초 생성
 """

r, c, t = map(int, input().split())
graph = [
    list(map(int, input().split()))
    for _ in range(r)
]
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]

# 공기청정기 위치 파악
def find_clean():
    for i in range(r):
        if graph[i][0] == -1:
            return i, i - 1

# 행 값 반환
clean_up, clean_down, = find_clean()
# 확산
while t:  # t초 동안
    print("==========================================")
    tmp_arr = [[0] * c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if graph[i][j] > 0:
                tmp = 0
                for k in range(4):
                    nx, ny = i + dx[k], j + dy[k]
                    if 0 <= nx < r and 0 <= ny < c and graph[nx][ny] != -1:
                        tmp_arr[nx][ny] += graph[i][j] // 5
                        tmp += graph[i][j] // 5
                print(f"tmp = {tmp}")
                graph[i][j] -= tmp
    for i in range(r):
        for j in range(c):
            graph[i][j] += tmp_arr[i][j]
    print(f"graph = {graph}")
    
    t -= 1
