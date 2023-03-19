"""
 *packageName    : 
 * fileName       : 20955.민서의 응급 수술
 * author         : ipeac
 * date           : 2023-03-06
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2023-03-06        ipeac       최초 생성
"""
import sys
from collections import deque

n, m = map(int, sys.stdin.readline().rstrip().split())
graph = [[] for _ in range(n + 1)]
for i in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
visited = [0] * (n + 1)

cnt = 0
edge = 0
for i in range(1, n + 1):
    if not visited[i]:
        cnt += 1
        
        visited[i] = True
        q = deque()
        q.append(i)
        while q:
            x = q.popleft()
            for value in graph[x]:
                if not visited[value]:
                    visited[value] = True
                    edge += 1
                    q.append(value)
# 끊겨있는 트리를 연결할때는 .. 트리 수 -1 만큼의 간선이 필요합니다 + 그래프형식으로 순환하는 예비 트리가 존재하는 경우 끊어줘야합니다.
# edge 의 경우 방문한 곳은 들르지 않기에 본래 트리에서 요하는 간선만 담겨있을겁니다. -> 그렇기에 실제 m -> 간선의 개수에서 사용하는 간선을 빼주면 없어져야하는 간선의 개수를 구할 수 있습니다.
print(cnt - 1 + (m - edge))
