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
            if color != graph[i][j]:  # 범위안에 한개라도 다른 경우.. 4분면으로 나눠서 다시 검색한다.
                result.append("(")
                quad_tree(x, y, n // 2)
                quad_tree(x, y + n // 2, n // 2)
                quad_tree(x + n // 2, y, n // 2)
                quad_tree(x + n // 2, y + n // 2, n // 2)
                result.append(")")
                return
    result.append(color)  # 재귀 x 범위안의 모든 수가 같으면 color 숫자를 담는다.

quad_tree(0, 0, n)
print("".join(map(str, result)))
