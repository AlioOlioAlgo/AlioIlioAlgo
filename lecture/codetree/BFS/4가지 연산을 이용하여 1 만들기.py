"""
 *packageName    : 
 * fileName       : 4가지 연산을 이용하여 1 만들기
 * author         : ipeac
 * date           : 2023-02-27
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2023-02-27        ipeac       최초 생성
 """
from collections import deque

n = int(input())
dx = [1, -1, 2, 3]
arr = [0 for i in range(1, 2 * n + 2)]  # arr 에 숫자에 대한 최솟count를 저장합니다
visited = [False for _ in range(1, 2 * n + 2)]

def can_go(x):
    return in_range(x) and not visited[x]

def in_range(x):
    return 1 <= x < 2 * n + 1

def bfs():
    q = deque()
    q.append(1)
    visited[1] = True
    print(f"q  ==> {q}")
    
    while q:
        x = q.popleft()
        for i in range(4):
            if i == 0 or i == 1:
                nx = x + dx[i]
            else:
                nx = x * dx[i]
            if in_range(nx) and can_go(nx):
                print(f"nx  ==> {nx}")
                visited[nx] = True
                q.append(nx)
                arr[nx] = arr[x] + 1
            if nx == n:
                print(arr[nx])
                return

bfs()
