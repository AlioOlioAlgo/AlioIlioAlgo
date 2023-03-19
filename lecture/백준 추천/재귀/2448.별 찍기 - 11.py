"""
 *packageName    :
 * fileName       : 2448.별 찍기 - 11
 * author         : ipeac
 * date           : 2023-03-12
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2023-03-12        ipeac       최초 생성
"""
import sys

sys.setrecursionlimit(10 ** 5)
n = int(input())
star = [
    [' ' for _ in range(2 * n - 1)]
    for _ in range(n)
]

def make_tree(n, x, y):
    if n <= 3:
        star[x][y] = '*'
        star[x + 1][y - 1] = '*'
        star[x + 1][y + 1] = '*'
        star[x + 2][y - 2] = '*'
        star[x + 2][y + 2] = '*'
        star[x + 2][y - 1] = '*'
        star[x + 2][y] = '*'
        star[x + 2][y + 1] = '*'
        return
    make_tree(n // 2, x, y)
    make_tree(n // 2, x + n // 2, y - n // 2)
    make_tree(n // 2, x + n // 2, y + n // 2)

make_tree(n, 0, n - 1)
for line in star:
    print(''.join(line))
