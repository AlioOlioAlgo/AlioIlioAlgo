"""
 *packageName    : 
 * fileName       : 박상준2
 * author         : ipeac
 * date           : 2022-10-28
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-10-28        ipeac       최초 생성
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

def div_con(x, y, n):
    global result
    color = graph[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            # 색이 달라진다면 바로 사분면 나눠서 검색한다.
            if color != graph[i][j]:
                result.append('(')
                div_value = n // 2
                div_con(x, y, div_value)
                div_con(x, y + div_value, div_value)
                div_con(x + div_value, y, div_value)
                div_con(x + div_value, y + div_value, div_value)
                result.append(')')
                return
    result.append(color)

div_con(0, 0, n)
print(result)
