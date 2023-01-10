"""
 *packageName    :
 * fileName       : 최적의 십자 모양 폭발
 * author         : ipeac
 * date           : 2023-01-10
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2023-01-10        ipeac       최초 생성
 """
from pprint import pprint

n = int(input())

graph = [
    list(map(int, input().split()))
    for _ in range(n)
]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

pprint(graph, width=50)

def rotate(cnt, target_graph):
    for _ in range(cnt):
        target_graph = [list(num[::-1]) for num in zip(*target_graph)]
        print(f"graph = {graph}")
    return target_graph

def bomb(row, col):
    global tmp_graph
    spread_num = tmp_graph[row][col]
    tmp_graph[row][col] = 0
    for k in range(4):
        x, y = row, col
        print(f"x, y = {x, y}")
        for i in range(spread_num - 1):
            x, y = x + dx[k], y + dy[k]
            if x < 0 or x >= n or y < 0 or y >= n:
                break
            tmp_graph[x][y] = 0
    print("펑")
    pprint(tmp_graph, width=50)
    
    tmp_graph = rotate(1, tmp_graph)
    print("로테이트")
    pprint(tmp_graph, width=50)
    
    # 0부분 왼쪽으로 밀기
    for idx in range(len(tmp_graph)):
        cursor = 0
        
        tmp_line = [0 for _ in range(n)]
        for value in (tmp_graph[idx]):
            if value:
                tmp_line[cursor] = value
                cursor += 1
        tmp_graph[idx] = tmp_line[:]
    print("밀기")
    pprint(tmp_graph, width=50)

pprint(graph, width=50)

max_pair = 0

for i in range(n):
    for j in range(n):
        tmp_graph = [num[:] for num in graph]
        
        bomb(i, j)
        tmp_graph = rotate(3, tmp_graph)
        print("터지고 밀고")
        pprint(tmp_graph, width=50)
        print("==========================================")
        
        cnt = 0
        for a in range(n):
            for b in range(n - 1):
                if tmp_graph[a][b] and tmp_graph[a][b] == tmp_graph[a][b + 1]:
                    cnt += 1
        
        for a in range(n - 1):
            for b in range(n):
                if tmp_graph[a][b] and tmp_graph[a][b] == tmp_graph[a + 1][b]:
                    cnt += 1
        max_pair = max(cnt, max_pair)
        print(f"max_pair = {max_pair}")
print(max_pair)
