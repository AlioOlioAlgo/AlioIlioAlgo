"""
 *packageName    :
 * fileName       : 박상준
 * author         : ipeac
 * date           : 2022-10-25
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-10-25        ipeac       최초 생성
 """
from collections import deque

# 세로 가로 길이
m, n = map(int, input().split())
graph = [
    list(map(int, input().split()))
    for _ in range(m)
]
# print(f"m,n = {m, n}")
# print(f"graph = {graph}")

dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]

# m, n = (13, 12)
# graph = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0], [0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0], [0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0],
#          [0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0], [0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0], [0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0], [0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0], [0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0], [0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
#          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
cheese = []

# 겉돌기 가다가 1 만나면 큐에 담지않고 0으로 바꿔주기만 한다. > 나머지 순회
def bfs(i, j):
    q = deque([[i, j]])  # 큐에 초기 방문할 0,0 을 담는다.
    visited = [[0] * n for _ in range(m)]
    visited[i][j] = 1
    cnt = 0
    while q:
        x, y = q.popleft()
        for xx, yy in zip(dx, dy):  # 4방향 순회
            nx, ny = xx + x, yy + y
            if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:  # 배열밖으로 나가지않으며, 한번 방문한 곳은 다시 돌지않는다,
                if graph[nx][ny] == 0:  # 치즈가 없다면 안심하고 방문처리 + 디큐에 다음 이동 장도를 담아준다.
                    visited[nx][ny] = 1
                    q.append([nx, ny])
                elif graph[nx][ny] == 1:  # 치즈가 있는 경우 방문처리 + cnt 로 현재 이 치즈판에 몇개의 치즈가 있는지 체크할 cnt +1 || 치즈를 0으로 만들어주고 || 큐에는 담지않는다. ( 제일 밖에있는 치즈만 없애줘야하기 때문)
                    visited[nx][ny] = 1
                    cnt += 1
                    graph[nx][ny] = 0
    cheese.append(cnt)  # 남은 치즈수를 기억하기 위함.
    return cnt

ans = 0
while True:
    ans += 1
    if bfs(0, 0) == 0:  # 판의 가장자리 부터 순회 >  cnt 가 0이 되는 순간 치즈가 없으므로 반복문 종료
        break
print(ans - 1)  #
print(cheese[-2])  # 마지막 전단계 cnt 출력
