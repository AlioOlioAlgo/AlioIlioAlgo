"""
 *packageName    : 
 * fileName       : 1992.쿼드트리
 * author         : ipeac
 * date           : 2023-03-05
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2023-03-05        ipeac       최초 생성
"""
n = int(input())
colors = [
    list(map(int, input()))
    for _ in range(n)
]

def div_conquer(x, y, n):
    if n == 1:
        return str(colors[x][y])
    color = colors[x][y]
    
    for i in range(x, x + n):
        for j in range(y, y + n):
            if color != colors[i][j]:
                return "(" + div_conquer(x, y, n // 2) + div_conquer(x, y + n // 2, n // 2) + div_conquer(x + n // 2, y, n // 2) + div_conquer(x + n // 2, y + n // 2, n // 2) + ")"
    
    return str(colors[x][y])

print(div_conquer(0, 0, n))
