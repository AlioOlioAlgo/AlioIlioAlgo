"""
 *packageName    : 
 * fileName       : 숨바꼭질4
 * author         : ipeac
 * date           : 2023-03-05
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2023-03-05        ipeac       최초 생성
"""
from collections import deque

n, k = map(int, input().split())
ans = 1e9

def trace_path(start, end, parent):
    path = []
    while end != start:
        path.append(end)
        end = parent[end]
    path.append(start)
    return path[::-1]

def bfs():
    visited = [False] * 100001
    parent = [-1] * 100001
    result = []
    q = deque()
    q.append((n, 0))
    result.append(n)
    visited[n] = True
    while q:
        cur, cnt = q.popleft()
        if cur == k:
            path = trace_path(n, k, parent)
            print(cnt)
            print(' '.join(map(str, path)))
            break
        if cur - 1 >= 0 and not visited[cur - 1]:
            visited[cur - 1] = True
            parent[cur - 1] = cur
            q.append((cur - 1, cnt + 1))
        if cur + 1 < 100001 and not visited[cur + 1]:
            visited[cur + 1] = True
            parent[cur + 1] = cur
            q.append((cur + 1, cnt + 1))
        if cur * 2 < 100001 and not visited[cur * 2]:
            visited[cur * 2] = True
            parent[cur * 2] = cur
            q.append((cur * 2, cnt + 1))

bfs()
