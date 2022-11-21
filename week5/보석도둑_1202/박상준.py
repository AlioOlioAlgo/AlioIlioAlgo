"""
 *packageName    :
 * fileName       : 박상준
 * author         : ipeac
 * date           : 2022-11-21
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-11-21        ipeac       최초 생성
 """
n, k = map(int, input().split())
jew = [list(map(int, input().split())) for _ in range(n)]
bag = [int(input()) for _ in range(k)]
jew.sort(key=lambda x: (x[0], -x[1]))
bag.sort()
print(f"jew = {jew}")
print(f"bag = {bag}")
