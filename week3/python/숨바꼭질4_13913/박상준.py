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
cnt = 0
visited = [0] * 100001
move = [0] * 100001
ans = deque()

def bfs(n):
    global cnt
    q = deque()
    q.append(n)
    
    while q:
        x = q.popleft()
        if x == k:
            cnt = visited[k]
            ans.append(str(k))
            v = k
            for i in range(cnt):
                value = move[v]
                ans.appendleft(str(value))
                v = value
            return
        if 0 <= x - 1 < 100001 and (not visited[x - 1] or visited[x - 1] == visited[x] + 1):
            q.append(x - 1)
            visited[x - 1] = visited[x] + 1
            move[x - 1] = x
        if 0 <= x + 1 < 100001 and (not visited[x + 1] or visited[x + 1] == visited[x] + 1):
            q.append(x + 1)
            visited[x + 1] = visited[x] + 1
            move[x + 1] = x
        if 0 <= 2 * x < 100001 and (not visited[2 * x] or visited[2 * x] == visited[x] + 1):
            q.append(2 * x)
            visited[2 * x] = visited[x] + 1
            move[2 * x] = x

bfs(n)
print(cnt)
print(' '.join(ans))
