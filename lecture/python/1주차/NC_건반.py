"""
 *packageName    :
 * fileName       : NC_건반
 * author         : ipeac
 * date           : 2022-11-21
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-11-21        ipeac       최초 생성
 """
from collections import deque

intel = [[1, 2], [1, 3], [2, 3], [3, 4], [4, 5], [3, 5], [5, 6], [5, 7], [6, 7], [7, 8], [8, 9], [8, 10], [9, 10], [10, 11], [10, 12], [11, 12]]

def solution(musics):
    graph = [[] * 13 for _ in range(13)]
    for inte in intel:
        graph[inte[0]].append(inte[1])
        graph[inte[1]].append(inte[0])
    # print(f"graph = {graph}")
    ans = 0
    
    def bfs(v, target):
        # print("==========================================")
        # print(f"v,target = {v, target}")
        visited = [0 for _ in range(13)]
        q = deque()
        q.append(v)
        visited[v] = 1
        # print(f"visited = {visited}")
        while q:
            x = q.popleft()
            if x == target:
                # print(f"visited = {visited[x] - 1}")
                return visited[x] - 1
            for k in graph[x]:
                if not visited[k]:
                    q.append(k)
                    visited[k] = visited[x] + 1
            # print(f"q = {q}")
    
    ans += bfs(1, musics[0])
    for idx in range(len(musics) - 1):
        ans += bfs(musics[idx], musics[idx + 1])
    print(ans)
    return ans

solution([10, 9, 4, 5, 12])
solution([6, 4, 2, 11])
