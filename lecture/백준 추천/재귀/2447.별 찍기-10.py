"""
 *packageName    : 
 * fileName       : 2447.별 찍기-10
 * author         : ipeac
 * date           : 2023-03-12
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2023-03-12        ipeac       최초 생성
"""

n = int(input())

def make_star(n, x, y):
    if n == 1:
        graph[x][y] = '*'
        return
    
    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                continue
            make_star(n // 3, x + i * n // 3, y + j * n // 3)

graph = [
    [' ' for _ in range(n)]
    for _ in range(n)
]
make_star(n, 0, 0)
for i in range(n):
    for j in range(n):
        print(graph[i][j], end="")
    print()
