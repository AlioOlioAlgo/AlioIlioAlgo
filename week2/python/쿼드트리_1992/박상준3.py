"""
 *packageName    :
 * fileName       : 박상준3
 * author         : ipeac
 * date           : 2022-11-08
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-11-08        ipeac       최초 생성
 """
n = int(input())
screen = [list(map(int, input())) for _ in range(n)]
# print(f"screen = {screen}")
# screen = [[1, 1, 1, 1, 0, 0, 0, 0], [1, 1, 1, 1, 0, 0, 0, 0], [0, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 1, 1, 1, 0, 0], [1, 1, 1, 1, 0, 0, 0, 0], [1, 1, 1, 1, 0, 0, 0, 0], [1, 1, 1, 1, 0, 0, 1, 1], [1, 1, 1, 1, 0, 0, 1, 1]]
result = ''

def div(start, end, nv):
    global result
    first_color = screen[start][end]
    for i in range(start, start + nv):
        for j in range(end, end + nv):
            if first_color != screen[i][j]:
                div_value = nv // 2
                result += '('
                div(start, end, div_value)
                div(start, end + div_value, div_value)
                div(start + div_value, end, div_value)
                div(start + div_value, end + div_value, div_value)
                result += ')'
                return
    # 다 같은 경우 하나로 압축이 가능하기에 .
    result += str(first_color)

div(0, 0, len(screen[0]))
print(result)
