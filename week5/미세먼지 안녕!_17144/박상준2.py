"""
 *packageName    :
 * fileName       : 박상준2
 * author         : ipeac
 * date           : 2022-11-28
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-11-28        ipeac       최초 생성
 """
r, c, t = map(int, input().split())  # r  세로   c   가로   t   초 가 지난 후
graph = [
    list(map(int, input().split()))
    for _ in range(r)
]
for _ in range(t):
    dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
    # 공기청정기의 위치 파악
    up = 0
    down = 0
    a = [item[:] for item in graph]  # 그래프의 확산을 기록하기 위한 2차원 배열의 복사 ( 동시적인 확산 때문 )
    # 확산 돌면서 공기청정기의 위치를 파악하고 확산 배열도 만들어줌
    for row in range(r):
        for col in range(c):
            # print("==========================================")
            if graph[row][col] == -1 and up == 0 and down == 0:  # 공기청정기의 위치를 기록한다. 한번만 기록하기위해 2 , 3 조건을 설정하였다.
                print("위치")
                print(f"row, col = {row, col}")
                up = row
                down = row - 1
            elif graph[row][col] > 0:  # 미세 먼지가 존재 하는 경우
                # print(f"a[row][col] = {a[row][col]}")
                # 4방향으로 확산을 기록한다.
                tmp = 0
                for i in range(4):
                    nx, ny = row + dx[i], col + dy[i],
                    # print(f"nx, ny = {nx, ny}")
                    if 0 <= nx < r and 0 <= ny < c and graph[nx][ny] != -1:  # 그래프가 안에 있고, -1 공기청정기가 아니이여야 카운트를 늘려줌.
                        # print("확산")
                        # 확산량 해당 graph [row][col] 값의 //5
                        a[nx][ny] += graph[row][col] // 5
                        # 확산한 량을 기록하여 tmp 에 남김
                        tmp += graph[row][col] // 5
                        # print(f"tmp = {tmp}")
                # 그 값을 a에서 빼준다,
                a[row][col] -= tmp
                # print(f"a[row][col] = {a[row][col]}")
    graph = a  # 얕은 복사
    print(f"graph = {graph}")
    # 확산끝
    #
    # 4방향으로 확산한다. 위 기준    우 상 좌 하
    # 아래 기준   우 하 좌 상
    dx = [0, -1, 0, 1]
    dy = [1, 0, -1, 0]
    # start 지점 graph[up][0] 우-->
    # print(f"up = {up}")
    prev = 0
    x, y = up, 1  # 시작위치
    k = 0
    while True:
        if k > 3:
            break
        nx, ny = x + dx[k], y + dy[k],
        if nx == up and ny == 0:  # 공기청정기를 만나면 반복문을 종료한다.
            break
        if not 0 <= nx < r or not 0 <= ny < c:  # 앞으로 삐져나가면 원래 값으로 변경해주고 방향 전환
            # print("삐져나옴")
            nx, ny = nx - dx[k], ny - dy[k]
            k += 1
            # print(f"nx, ny = {nx, ny}")
            # print(f"k = {k}")
            # print("==========================================")
            continue
        # print("바꿈")
        # print(f"prev = {prev}")
        # print(f"nx, ny = {nx, ny}")
        # print(f"graph[nx][ny] = {graph[nx][ny]}")
        prev, graph[nx][ny] = graph[nx][ny], prev
        # print(f"prev = {prev}")
        x, y = nx, ny
    print(f"graph = {graph}")
    
    print("==========================================")
    # 아래 기준   우 하 좌 상
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    
    # print(f"down = {down}")
    prev = 0
    x, y = down, 1
    k = 0
    while True:
        if k > 3:
            break
        nx, ny = x + dx[k], y + dy[k],
        if nx == down and ny == 0:  # 공기청정기를 만나면 반복문을 종료한다.
            break
        if not 0 <= nx < r or not 0 <= ny < c:  # 앞으로 삐져나가면 원래 값으로 변경해주고 방향 전환
            # print("삐져나옴")
            nx, ny = nx - dx[k], ny - dy[k]
            k += 1
            # print(f"nx, ny = {nx, ny}")
            # print(f"k = {k}")
            # print("==========================================")
            continue
        print("바꿈")
        print(f"prev = {prev}")
        print(f"nx, ny = {nx, ny}")
        print(f"graph[nx][ny] = {graph[nx][ny]}")
        prev, graph[nx][ny] = graph[nx][ny], prev
        # print(f"prev = {prev}")
        x, y = nx, ny,
    print(f"graph = {graph}")
ans = 0
for item in graph:
    ans += sum(item)
print(ans)
