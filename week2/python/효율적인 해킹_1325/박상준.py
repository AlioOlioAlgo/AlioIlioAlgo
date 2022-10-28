"""
 *packageName    : 
 * fileName       : 박상준
 * author         : ipeac
 * date           : 2022-10-26
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-10-26        ipeac       최초 생성
 """
import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    # graph[a].append(b)
    graph[b].append(a)

# print(f"n,m = {n, m}")
# print(f"graph = {graph}")

# n, m = (5, 4)
# graph = [[], [3], [3], [4, 5], [], []]

def bfs(start):
    visited = [0 for _ in range(n + 1)]
    q = deque()
    q.append(start)
    cnt = 1
    visited[start] = 1
    while q:
        x = q.popleft()
        for i in graph[x]:
            if not visited[i]:
                q.append(i)
                visited[i] = 1
                cnt += 1
    return cnt

max_cnt = 0
max_arr = []
for i in range(1, len(graph)):
    res = bfs(i)
    max_arr.append([i, res])
    max_cnt = max(res, max_cnt)
for i, v in max_arr:
    if v == max_cnt:
        print(i, end=" ")
