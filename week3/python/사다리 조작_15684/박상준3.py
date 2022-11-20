"""
 *packageName    :
 * fileName       : 박상준3
 * author         : ipeac
 * date           : 2022-11-10
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-11-10        ipeac       최초 생성
 """
n, m, h = 5, 5, 6  # n ;세로선 m 가로선 ; h ; 세로선마다 가로선을 놓을 수 있는 위치의 개수 H
graph = [[0] * (n + 1) for _ in range(h + 1)]

# for i in range(m):
#     a, b = map(int, input().split())
#     graph[a][b] = 1  # 1 시작점
#     graph[a][b + 1] = -1  # -1 끝점
# print(f"graph = {graph}")

graph = [[0, 0, 0, 0, 0, 0], [0, 1, -1, 0, 0, 0], [0, 0, 0, 1, -1, 0], [0, 0, 1, -1, 0, 0], [0, 0, 0, 0, 0, 0], [0, 1, -1, 0, 1, -1], [0, 0, 0, 0, 0, 0]]

# i부터 시작해서  i로 끝나는지 모든 컬럼을 체크합니다.
def check_right():
    for row in range(1, h + 1):
        start = row
        for col in range(1, n + 1):
            # 가는중에 가로선의 왼쪽을 만난다면 start 를 +1
            if graph[row][col] == 1:
                start += 1
            # 가로선의 오른쪽을 만난다면 start를  -1
            elif graph[row][col] == -1:
                start -= 1
        # 만약 row != start 라면 틀린놈임.
        if row != start:
            return False
    return True

# to_choose : 남은 라인수 # line_cnt  놓아진 라인 카운트
def make_line(x, y, cnt):
    global ans
    if ans <= cnt:  # 가로선을 정답보다 많이 만든 경우 확인 필요 x > 우리는 최솟값만 필요하다!
        return
    if check_right():
        ans = min(ans, cnt)  # 저장
        return
    if cnt == 3:  # 3가 3인 경우 이제 가로선을 놓으면 안되기에 종료한다.
        return
    for i in range(1, h + 1):
        for j in range(1, n + 1):
            if graph[i][j] == 0 and graph[i][j + 1] == 0:
                graph[i][j] = 1
                graph[i][j + 1] = -1
                make_line(x, y + 2, cnt + 1)
                graph[i][j] = 0
                graph[i][j + 1] = 0

ans = 4
make_line(1, 1, 0)

print(ans if ans <= 3 else -1)
