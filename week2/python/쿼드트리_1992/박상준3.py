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
n = 8
# screen = [list(map(int, input())) for _ in range(n)]
# print(f"screen = {screen}")
screen = [[1, 1, 1, 1, 0, 0, 0, 0], [1, 1, 1, 1, 0, 0, 0, 0], [0, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 1, 1, 1, 0, 0], [1, 1, 1, 1, 0, 0, 0, 0], [1, 1, 1, 1, 0, 0, 0, 0], [1, 1, 1, 1, 0, 0, 1, 1], [1, 1, 1, 1, 0, 0, 1, 1]]

# 해당 구역안에서 같은 값만이 존재하지 않는다면
def check(start, end, nv):
    first_value = screen[start][end]
    for i in range(start, start + nv):
        for j in range(end, end + nv):
            if first_value != screen[i][j]:
                return False
    return True

def div():
    pass
