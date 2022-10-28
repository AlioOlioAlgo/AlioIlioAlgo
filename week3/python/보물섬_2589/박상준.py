"""
 *packageName    :
 * fileName       : 박상준
 * author         : ipeac
 * date           : 2022-10-28
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-10-28        ipeac       최초 생성
 """
from collections import deque

n, m = map(int, input().split())
treasure_map = [
    list(map(str, input()))
    for _ in range(n)
]

# print(f"n,m = {n, m}")
# print(f"treasure_map = {treasure_map}")

dx, dy = [0, 0, 1, -1], [1, -1, 0, 0],

# input = sys.stdin.readline

# n, m = (5, 7)
# treasure_map = [['W', 'L', 'L', 'W', 'W', 'W', 'L'], ['L', 'L', 'L', 'W', 'L', 'L', 'L'], ['L', 'W', 'L', 'W', 'L', 'W', 'W'], ['L', 'W', 'L', 'W', 'L', 'L', 'L'], ['W', 'L', 'L', 'W', 'L', 'W', 'W']]

def bfs(i, j):
    visited = [[0] * m for _ in range(n)]
    q = deque()
    q.append([i, j])
    visited[i][j] = 1
    
    while q:
        x, y = q.popleft()
        for xx, yy in zip(dx, dy):
            nx, ny = xx + x, yy + y
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and treasure_map[nx][ny] == 'L':
                # 거리값을 기록한다.
                visited[nx][ny] = visited[x][y] + 1
                q.append([nx, ny])
    # 처음 위치 -> 제일 멀리갈 수 있는 위치를 리턴한다.
    return max(map(max, visited))

max_value = []
for i in range(n):
    for j in range(m):
        if treasure_map[i][j] == 'L':
            # 제일 멀리 갈 수 있는 위치 리턴받은 값중에 가장 긴 값이 육지에서의 보물간의 거리이다.
            # 이미 bfs 로 탐색했기에 최단거리이기에 가장 긴 값을 그냥 출력하면됨 ㅇㅇ.
            #
            # 시간초과 발생으로 로직 수정 -> 60 퍼 에서 멈춤 ㅅㅂ -> 찾아보니 pypy3 로 다 냈길래 그냥 파이더블로 ㄱㄱ
            # max_value = max(max_value, bfs(i, j))
            max_value.append(bfs(i, j))
print(max(max_value) - 1)
