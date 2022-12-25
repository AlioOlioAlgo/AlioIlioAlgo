"""
 *packageName    :
 * fileName       : 박상준
 * author         : ipeac
 * date           : 2022-12-25
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-12-25        ipeac       최초 생성
 """
X, Y = map(int, input().split())  # X 게임 횟수 Y 이긴 게임
# 앞으로의 모든 게임에서 지지 않는다.
Z = Y * 100 // X
print(f"Z = {Z}")
ans = 0
min_value, max_value = 0, 1000000000
while min_value <= max_value:
    mid = (min_value + max_value) // 2
    if (Y + mid) * 100 // (X + mid) > Z:
        max_value = mid - 1
        ans = mid
    else:
        min_value = mid + 1
print(f"ans = {ans}")
