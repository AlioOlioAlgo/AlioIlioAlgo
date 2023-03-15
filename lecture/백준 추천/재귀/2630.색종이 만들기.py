"""
 *packageName    : 
 * fileName       : 2630.색종이 만들기
 * author         : ipeac
 * date           : 2023-03-13
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2023-03-13        ipeac       최초 생성
"""
n = int(input())
graph = [
    list(map(int, input().split()))
    for _ in range(n)
]
white = 0
blue = 0

def make_same(piece, x, y):
    global white
    global blue
    if piece == 1:
        if graph[x][y] == 1:
            blue += 1
        elif graph[x][y] == 0:
            white += 1
        return
    div = piece // 2
    for i in range(x, x + piece):
        for j in range(y, y + piece):
            if graph[i][j] != graph[x][y]:
                make_same(div, x, y)
                make_same(div, x + div, y)
                make_same(div, x, y + div)
                make_same(div, x + div, y + div)
                return
    if graph[x][y] == 1:
        blue += 1
    elif graph[x][y] == 0:
        white += 1
    return

make_same(n, 0, 0)
print(white)
print(blue)
