"""
 *packageName    :
 * fileName       : 박상준
 * author         : ipeac
 * date           : 2022-12-08
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-12-08        ipeac       최초 생성
 """
n = int(input())

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

ans = 0

arr = [[0] * 101 for _ in range(101)]  # 드래곤 커브를 기록할 2차원 배열 100* 100
print(f"arr = {arr}")

for _ in range(n):
    print("==========================================")
    # x, y : 드래곤 커브의 시작점 , d : 커브의 시작지점,  g : 세대
    x, y, d, g = map(int, input().split())
    arr[x][y] = 1  # 처음 시작지점을 기록한다.
    
    move = [d]  # 처음 선분이 이어지는 방향
    
    # g 세대 만큼 반복한다.
    for _ in range(g):
        tmp = []
        for i in range(len(move)):
            tmp.append((move[-i - 1] + 1) % 4)  # 이전 세대 값에서 반대서부터 +1 한 값을 뒤에 무빙할 값으로 extend해서 모두 기록해준다.
        move.extend(tmp)
    
    # 드래곤 배열에 기록한다.
    for i in move:
        nx = x + dx[i]
        ny = y + dy[i]
        arr[nx][ny] = 1
        x, y = nx, ny

for i in range(100):
    for j in range(100):
        if arr[i][j] and arr[i + 1][j] and arr[i + 1][j + 1] and arr[i][j + 1]:
            ans += 1
print(ans)
