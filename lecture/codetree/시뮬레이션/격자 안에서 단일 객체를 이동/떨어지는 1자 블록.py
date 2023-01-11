"""
 *packageName    :
 * fileName       : 떨어지는 1자 블록
 * author         : ipeac
 * date           : 2023-01-11
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2023-01-11        ipeac       최초 생성
 """
n, m, k = map(int, input().split())
graph = [
    list(map(int, input().split()))
    for _ in range(n)
]

start_block = k - 1
end_block = k + m - 2
# print(f"start_block = {start_block}")
# print(f"end_block = {end_block}")
x = 0
check = False
for i in range(n):
    if check:
        break
    graph_line = graph[i]
    for j in range(n):
        if start_block <= j <= end_block:
            if graph[i][j] == 1:
                check = True
                break
    else:
        x = i
# print(f"x = {x}")
for i in range(start_block, end_block + 1):
    graph[x][i] = 1
for num in graph:
    print(*num)
