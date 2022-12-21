"""
 *packageName    :
 * fileName       : 박상준2
 * author         : ipeac
 * date           : 2022-12-21
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-12-21        ipeac       최초 생성
 """
n = int(input())

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

# 드래곤 커브 그래프 100*100
graph = [[0] * 101 for _ in range(101)]
ans = 0
for _ in range(n):
    # x => 좌표 y => 좌표 || d => 시작방향, g => 세대
    x, y, d, g = map(int, input().split())
    graph[x][y] = 1  # 처음 시작지점 기록
    
    move = [d]  # 처음 선분이 이어지는 방향
    
    # g 세대 만큼 반복함
    for _ in range(g):
        tmp = []
        for i in range(len(move)):
            tmp.append((move[-i - 1] + 1) % 4)
        move.extend(tmp)
    
    # 드래곤 배열에 기록한다.
    for i in move:
        nx, ny = x + dx[i], y + dy[i]
        graph[nx][ny] = 1
        x, y = nx, ny

for i in range(100):
    for j in range(100):
        if graph[i][j] and graph[i + 1][j] and graph[i][j + 1] and graph[i + 1][j + 1]:
            ans += 1
print(ans)
