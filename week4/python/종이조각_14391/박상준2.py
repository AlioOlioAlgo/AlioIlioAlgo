"""
 *packageName    :
 * fileName       : 박상준2
 * author         : ipeac
 * date           : 2022-11-23
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-11-23        ipeac       최초 생성
 """
n, m = map(int, input().split())  # n  세로    m   가로
arr = [list(map(int, input())) for _ in range(n)]

max_ans = 0

def bitmask():
    global max_ans
    # 비트마스크로 2 ^ (N * M )
    pass

bitmask()
print(max_ans)
