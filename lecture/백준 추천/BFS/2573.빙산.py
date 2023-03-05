"""
 *packageName    : 
 * fileName       : 2573.빙산
 * author         : ipeac
 * date           : 2023-03-05
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2023-03-05        ipeac       최초 생성
"""
# 빙산이 두 덩어리 이상으로 분리되는 최초의 시간
n, m = map(int, input().split())

graph = [
    list(map(int, input().split()))
    for _ in range(n)
]
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]

# 주변 빙산을 체크하는 함수
def check_iceburg(x, y):
    pass
