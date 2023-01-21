"""
 *packageName    :
 * fileName       : 1차원 바람
 * author         : ipeac
 * date           : 2022-12-30
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-12-30        ipeac       최초 생성
 """
from collections import deque

n, m, q = map(int, input().split())

graph = [
    deque(list(map(int, input().split())))
    for _ in range(n)
]

def rotate_way(target_row, side):
    if side == 'L':
        graph[target_row - 1].rotate(1)
    else:
        graph[target_row - 1].rotate(-1)

for _ in range(q):
    e_row, dir = map(str, input().split())  # 3 L
    e_row = int(e_row)
    tmp_dir = dir
    # print(f"e_row,dir = {e_row, dir}")
    # 해당 방향으로 로테이트
    rotate_way(e_row, dir)
    # print(f"graph = {graph}")
    # 위쪽 비교
    for i in range(e_row - 2, -1, -1):
        # print("위")
        # print(f"i = {i}")
        check_same = False
        for j in range(m):
            if graph[i][j] == graph[i + 1][j]:
                check_same = True
                break
        
        if not check_same:
            break
        else:
            if dir == 'L':
                dir = 'R'
            else:
                dir = 'L'
        rotate_way(i + 1, dir)  # 바뀐 방향으로 로테이트
        # print(f"graph = {graph}")
    # i 행을 반대로 rotate
    # 아래쪽 비교
    dir = tmp_dir
    for i in range(e_row, n):
        # print("아래")
        # print(f"i = {i}")
        check_same = False
        for j in range(m):
            if graph[i][j] == graph[i - 1][j]:
                check_same = True
                break
        
        if not check_same:
            break
        else:
            if dir == 'L':
                dir = 'R'
            else:
                dir = 'L'
            rotate_way(i + 1, dir)  # 바뀐 방향으로 로테이트
            # print(f"graph = {graph}")
for line in graph:
    print(*line)
