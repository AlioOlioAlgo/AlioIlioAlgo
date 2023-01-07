"""
 *packageName    :
 * fileName       : 박상준2
 * author         : ipeac
 * date           : 2023-01-07
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2023-01-07        ipeac       최초 생성
 """
import pprint
from itertools import permutations

n, m, s = map(int, input().split())
graph = [
    list(map(int, input().split()))
    for _ in range(n)
]
rotate_list = [
    list(map(int, input().split()))
    for _ in range(s)
]

def rotate(start_row, start_col, end_row, end_col):
    global tmp_graph
    temp = tmp_graph[start_row][start_col]
    
    for row in range(start_row, end_row):
        tmp_graph[row][start_col] = tmp_graph[row + 1][start_col]
    
    for col in range(start_col, end_col):
        tmp_graph[end_row][col] = tmp_graph[end_row][col + 1]
    
    for row in range(end_row, start_row, -1):
        tmp_graph[row][end_col] = tmp_graph[row - 1][end_col]
    
    for col in range(end_col, start_col + 1, -1):
        tmp_graph[start_row][col] = tmp_graph[start_row][col - 1]
    
    tmp_graph[start_row][start_col + 1] = temp

total_min = int(1e9)
for combi_list in permutations(rotate_list, s):
    print(f"combi_list = {combi_list}")
    tmp_graph = [num[:] for num in graph]
    pass
    for combi in combi_list:
        r, c, re = combi[0], combi[1], combi[2]
        r = r - 1
        c = c - 1
        now = tmp_graph[r][c]
        
        for i in range(1, re + 1):
            rotate(r - i, c - i, r + i, c + i)
            pprint.pprint(tmp_graph)
    for value_list in tmp_graph:
        total_min = min(total_min, sum(value_list))
print(total_min)
