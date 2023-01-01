"""
 *packageName    :
 * fileName       : 박상준2
 * author         : ipeac
 * date           : 2022-12-18
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-12-18        ipeac       최초 생성
 """
n = int(input())  # 보드의 크기
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
graph = [
    list(map(int, input().split()))
    for _ in range(n)
]
max_block = 0

def move(moved_graph, direction):
    if direction == 0:  # 우
        for x in range(n):  # x 쭉쭉
            cursor = n - 1
            for y in range(n - 1, -1, -1):
                if moved_graph[x][y] != 0:
                    tmp = moved_graph[x][y]
                    moved_graph[x][y] = 0
                    if moved_graph[x][cursor] == 0:
                        moved_graph[x][cursor] = tmp
                    elif moved_graph[x][cursor] != tmp:
                        cursor -= 1
                        moved_graph[x][cursor] = tmp
                    elif moved_graph[x][cursor] == tmp:
                        moved_graph[x][cursor] *= 2
                        cursor -= 1
    elif direction == 1:  # 좌
        for x in range(n):  # x 쭉쭉
            cursor = 0
            for y in range(n):
                if moved_graph[x][y] != 0:
                    tmp = moved_graph[x][y]
                    moved_graph[x][y] = 0
                    if moved_graph[x][cursor] == 0:
                        moved_graph[x][cursor] = tmp
                    elif moved_graph[x][cursor] != tmp:
                        cursor += 1
                        moved_graph[x][cursor] = tmp
                    elif moved_graph[x][cursor] == tmp:
                        moved_graph[x][cursor] *= 2
                        cursor += 1
    
    elif direction == 2:  # 남
        # print("==========================================")
        # print("남쪽으로 이동함")
        for y in range(n):  # x 쭉쭉
            cursor = n - 1
            for x in range(n - 1, -1, -1):
                if x == 0:
                    pass
                if moved_graph[x][y] != 0:
                    tmp = moved_graph[x][y]
                    moved_graph[x][y] = 0
                    if moved_graph[cursor][y] == 0:
                        moved_graph[cursor][y] = tmp
                    elif moved_graph[cursor][y] != tmp:
                        cursor -= 1
                        moved_graph[cursor][y] = tmp
                    elif moved_graph[cursor][y] == tmp:
                        moved_graph[cursor][y] *= 2
                        cursor -= 1
        # print(f"moved_graph = {moved_graph}")
    else:  # 북
        for y in range(n):  # x 쭉쭉
            cursor = 0
            for x in range(n):
                if moved_graph[x][y] != 0:
                    tmp = moved_graph[x][y]
                    moved_graph[x][y] = 0
                    if moved_graph[cursor][y] == 0:
                        moved_graph[cursor][y] = tmp
                    elif moved_graph[cursor][y] != tmp:
                        cursor += 1
                        moved_graph[cursor][y] = tmp
                    elif moved_graph[cursor][y] == tmp:
                        moved_graph[cursor][y] *= 2
                        cursor += 1
    return moved_graph

def bfs(graph, cnt):
    global max_block
    if cnt == 5:
        max_block = max(max_block, max(map(max, graph)))
        return
    else:
        for i in range(4):
            tmp_graph = [num[:] for num in graph]
            # # 0 동 1 서 2 남 3 북
            # if i == 2 and cnt == 0:
            #     print("==========================================")
            #     print("i==2")
            moved_graph = move(tmp_graph, i)
            bfs(moved_graph, cnt + 1)

bfs(graph, 0)
print(max_block)
