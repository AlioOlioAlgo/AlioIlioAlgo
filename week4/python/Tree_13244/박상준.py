"""
 *packageName    :
 * fileName       : 박상준
 * author         : ipeac
 * date           : 2022-11-12
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-11-12        ipeac       최초 생성
 """
from collections import deque

t = int(input())
for _ in range(t):
    n = int(input())  # 그래프의 노드수
    m = int(input())  # 그래프의 간선 수
    graph = [[] for _ in range(n + 1)]
    
    for i in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    
    # print(f"graph = {graph}")
    # 노드가 n  이라면 간선은  n-1
    #
    def bfs(start):
        visited = [0 for _ in range(n + 1)]
        q = deque()
        q.append(start)
        visited[start] = 1
        while q:
            x = q.popleft()
            for v in graph[x]:
                if not visited[v]:
                    q.append(v)
                    visited[v] = 1
        if visited[1:].count(0) >= 1:
            return False  # 전부 순회 불가능 > 그래프
        else:
            return True  # 트루 반환 => 전부 순회가능 > 트리
    
    check_cnt = 0
    for i in range(1, n + 1):
        if bfs(i):  # 트리 인경우
            pass
        else:
            check_cnt += 1
    if check_cnt >= 1:
        print('graph')
    else:
        if m == n - 1:
            print('tree')
        else:
            print('graph')
