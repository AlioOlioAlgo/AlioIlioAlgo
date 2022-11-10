"""
 *packageName    :
 * fileName       : 박상주
 * author         : ipeac
 * date           : 2022-11-06
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-11-06        ipeac       최초 생성
 """
from collections import deque

n, k = 5, 17
cnt = 0
visited = [0] * 500001
ans = deque()

def bfs(n):
    global cnt
    global k
    q = deque()
    q.append(n)
    plus = 0
    while q:
        x = q.popleft()
        if x == k:
            cnt = visited[k]
            return
        if 0 <= 2 * x < 500001 and (not visited[2 * x] or visited[2 * x] == visited[x] + 1):
            q.append(2 * x)
            visited[2 * x] = visited[x] + 1
        if 0 <= x - 1 < 500001 and (not visited[x - 1] or visited[x - 1] == visited[x] + 1):
            q.append(x - 1)
            visited[x - 1] = visited[x] + 1
        if 0 <= x + 1 < 500001 and (not visited[x + 1] or visited[x + 1] == visited[x] + 1):
            q.append(x + 1)
            visited[x + 1] = visited[x] + 1
        
        plus += 1
        k += plus

bfs(n)
print(cnt)
