"""
 *packageName    : 
 * fileName       : 그래프 탐색
 * author         : ipeac
 * date           : 2023-02-14
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2023-02-14        ipeac       최초 생성
"""

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

ans = 0

visited = [False for _ in range(n + 1)]
print(f"graph  ==> {graph}")

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
print(f"graph  ==> {graph}")

def dfs(vertex):
    global ans
    for cur in graph[vertex]:
        if not visited[cur]:
            visited[cur] = True
            ans += 1
            dfs(cur)

visited[1] = True
dfs(1)
print(ans)
