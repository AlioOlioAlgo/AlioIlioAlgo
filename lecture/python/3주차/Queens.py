"""
 *packageName    :
 * fileName       : Queens
 * author         : ipeac
 * date           : 2022-12-03
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-12-03        ipeac       최초 생성
 """
n, m = map(int, input().split())  # n  n* n 크기의 판이 존재한다.
remaining_queen = n - m
chess = [
    list(map(str, input().split()))
    for _ in range(n)
]
visited = [[0 for _ in range(n)] for _ in range(n)]
print(f"visited = {visited}")

for i in range(n):
    for j in range(n):
        if 'Q' == chess[i][j]:  # 체스 퀸 위치 방문 처리함
            visited[i][j] = 1

def check_queen(i, j):  # 해당위치에 queen 을 둔다면 조건에 부합하는지 체크한다.
    # 좌우 . 상하  . 좌우상 대각선 . 좌우하 대각선 고려
    if 'Q' in chess[i]:  # 행 비교
        return False
    
    # 열 비교
    for x in range(n):
        if chess[x][j] == 'Q':
            return False
    
    # 좌우상 좌우하 대각선
    dx = [1, 1, -1, -1]
    dy = [-1, 1, -1, 1]
    for k in range(4):
        nx, ny = i + dx[k], j + dy[k]
        while True:
            if 0 <= nx < n and 0 <= ny < n:
                if chess[nx][ny] == 'Q':
                    return False
            else:
                return False
            nx, ny = nx + dx[k], ny + dy[k]
    return True

ans = 0

def make_queen(start_row, start_col, cnt):
    global ans
    if cnt == m - n + 1:  # 퀸을 다 둔 경우
        ans += 1
        return
    for x in range(start_row, n):
        for y in range(start_col, n):
            if check_queen(x, y)
                pass

for i in range(n):
    for j in range(n):
        make_queen(i, j, m)
