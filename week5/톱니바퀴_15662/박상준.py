"""
 *packageName    :
 * fileName       : 박상준
 * author         : ipeac
 * date           : 2022-11-27
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-11-27        ipeac       최초 생성
 """
from collections import deque

T = int(input())
graph = [
    deque(list(map(int, input())))
    for _ in range(T)
]
K = int(input())
for i in range(K):
    print("====================()()()======================")
    R, L = map(int, input().split())  # R : 회전 횟수 . L 회전 방향
    a = [list(item)[:] for item in graph]
    # print(f"a = {a}")
    # R-1 인덱스 위치를 옮김
    if L == 1:
        graph[R - 1].rotate(1)
    
    else:
        graph[R - 1].rotate(-1)
    print("==========================================")
    # 이전 회전 여부
    left_L = L
    prev_rotate = True
    for idx in range(R - 2, -1, -1):
        print(f"idx + 1 = {idx + 1}")
        print(f"idx = {idx}")
        if a[idx + 1][6] != a[idx][2] and prev_rotate:
            if left_L == 1:
                graph[idx].rotate(-1)
                left_L = -1
            else:
                graph[idx].rotate(1)
                left_L = 1
            prev_rotate = True
        
        else:
            break
    print("==========================================")
    prev_rotate = True
    right_L = L
    for idx in range(R, T):
        print(f"idx = {idx}")
        print(f"idx-1 = {idx - 1}")
        if a[idx - 1][2] != a[idx][6] and prev_rotate:
            if right_L == 1:
                graph[idx].rotate(-1)
                right_L = -1
            else:
                graph[idx].rotate(1)
                right_L = 1
            prev_rotate = True
        else:
            break

ans = 0
for i in range(len(graph)):
    if graph[i][0] == 1:
        ans += 1
print(ans)
