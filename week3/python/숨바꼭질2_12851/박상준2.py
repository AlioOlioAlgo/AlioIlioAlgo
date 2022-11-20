"""
 *packageName    :
 * fileName       : 박상준2
 * author         : ipeac
 * date           : 2022-11-19
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-11-19        ipeac       최초 생성
 """
from collections import deque

n, k = map(int, input().split())
visited = [0 for _ in range(100001)]  # 모든 이동 경로 경우의 수 기입
value = 0  # 가장 빠른 방법으로 찾는 횟수
cnt = 0  # 최단 시간

def bfs(cur):  # 현재 위치 기록
    global cnt
    global value
    
    q = deque()
    q.append(cur)
    visited[cur] = 1
    
    while q:
        x = q.popleft()
        if x == k:
            cnt = visited[x]
            value += 1
            continue
        for operation in [2 * x, x - 1, x + 1]:
            if 0 <= operation < 100001 and (not visited[operation] or visited[operation] == visited[x] + 1):
                q.append(operation)
                visited[operation] = visited[x] + 1

bfs(n)
print(cnt - 1)
print(value)
