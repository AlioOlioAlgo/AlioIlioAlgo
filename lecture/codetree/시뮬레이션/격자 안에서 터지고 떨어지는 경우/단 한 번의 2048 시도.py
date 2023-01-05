"""
 *packageName    :
 * fileName       : 단 한 번의 2048 시도
 * author         : ipeac
 * date           : 2023-01-05
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2023-01-05        ipeac       최초 생성
 """

graph = [
    list(map(int, input().split()))
    for _ in range(4)
]

dir = input()

def down_block():
    global graph
    tmp_graph = [[0 for _ in range(4)] for _ in range(4)]
    # print(f"tmp_graph = {tmp_graph}")
    for col in range(4):
        cursor = 3
        tmp_value = -1
        
        for row in range(3, -1, -1):
            if not graph[row][col]:  # tmp_value
                continue
            if tmp_value == -1:
                tmp_value = graph[row][col]
            elif tmp_value == graph[row][col]:
                tmp_graph[cursor][col] = tmp_value * 2
                
                cursor -= 1
                tmp_value = -1
            else:
                tmp_graph[cursor][col] = tmp_value
                tmp_value = graph[row][col]
                
                cursor -= 1
        if tmp_value != -1:
            tmp_graph[cursor][col] = tmp_value
            cursor -= 1
    graph = [num[:] for num in tmp_graph]

def rotate(repeat, _graph):
    for _ in range(repeat):
        _graph = [k[::-1] for k in zip(*_graph[::])]
    return _graph

if dir == 'R':
    graph = rotate(1, graph)
    down_block()
    graph = rotate(3, graph)
elif dir == 'U':
    graph = rotate(2, graph)
    down_block()
    graph = rotate(2, graph)

elif dir == 'L':
    graph = rotate(3, graph)
    down_block()
    graph = rotate(1, graph)

else:
    down_block()
for num in graph:
    print(*num)
