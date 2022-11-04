"""
 *packageName    :
 * fileName       : 박상준
 * author         : ipeac
 * date           : 2022-11-02
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-11-02        ipeac       최초 생성
 """
from collections import deque

n, k = map(int, input().split())
# n, k = 5, 17
visited = [0] * 100001
cnt = 0
value = 0

def bfs(n):
    global cnt
    global value
    
    q = deque()
    q.append(n)
    visited[n] = 0
    while q:
        x = q.popleft()
        if x == k:
            cnt = visited[k]
            value += 1
            continue
        if 0 <= x - 1 < 100001 and (not visited[x - 1] or visited[x - 1] == visited[x] + 1):
            q.append(x - 1)
            visited[x - 1] = visited[x] + 1
        if 0 <= x + 1 < 100001 and (not visited[x + 1] or visited[x + 1] == visited[x] + 1):
            q.append(x + 1)
            visited[x + 1] = visited[x] + 1
        if 0 <= 2 * x < 100001 and (not visited[2 * x] or visited[2 * x] == visited[x] + 1):
            q.append(2 * x)
            visited[2 * x] = visited[x] + 1

bfs(n)
print(cnt)
print(value)
