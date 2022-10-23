"""
 *packageName    : 
 * fileName       : 박상준
 * author         : ipeac
 * date           : 2022-10-23
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-10-23        ipeac       최초 생성
 """
# n = int(input())
# graph = [
#     list(map(int, input()))
#     for _ in range(n)
# ]
# print(f"n = {n}")
# print(f"graph = {graph}")
n = 8
graph = [[1, 1, 1, 1, 0, 0, 0, 0], [1, 1, 1, 1, 0, 0, 0, 0], [0, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 1, 1, 1, 0, 0], [1, 1, 1, 1, 0, 0, 0, 0], [1, 1, 1, 1, 0, 0, 0, 0], [1, 1, 1, 1, 0, 0, 1, 1], [1, 1, 1, 1, 0, 0, 1, 1]]
result = []

def quad_tree(x, y, n):
    global result
    color = graph[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            # if color
            pass

quad_tree(0, 0, n)
print("".join(map(str, result)))
