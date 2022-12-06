"""
 *packageName    :
 * fileName       : 박상준
 * author         : ipeac
 * date           : 2022-12-06
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-12-06        ipeac       최초 생성
 """
from collections import deque

n = int(input())
graph = [
    deque(list(map(int, input().split())))
    for _ in range(n)
]
# graph = [[2, 2, 2], [4, 4, 4], [8, 8, 8]]
print(f"graph = {graph}")

def move(copyed_graph, direction):  # 0 동  1 서   2  북  3  남
    # copyed_graph  복사된 그래프,  direction  이동 방향
    if direction == 0:  # 동쪽으로 그래프를 이동시킨다.
        pass
    elif direction == 1:  # 서쪽으로 이동시킨다.
        pass
    elif direction == 2:
        pass
    elif direction == 3:
        pass
    
    return copyed_graph

ans = 0

def dfs(graph, cnt):  # 좌 우 상 하 이동 후 합치는 함수입니다. 해당 머지가 좌, 우 , 상  하 어디로 이동되었는지가 중요합니다.
    global ans
    if cnt == 5:
        ans = max(ans, max(map(max, graph)))
        return
    for i in range(4):  # 4방향으로 이동한 그래프를 생성한다.
        moved_graph = move(graph, i)
        pass

print(ans)
