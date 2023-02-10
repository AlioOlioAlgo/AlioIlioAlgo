"""
 *packageName    :
 * fileName       : 최소 점프 횟수
 * author         : ipeac
 * date           : 2023-01-31
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2023-01-31        ipeac       최초 생성
 """

n = int(input())
balls = list(map(int, input().split()))
min_cnt = 1e9

def in_range(x):
    return 0 <= x < n

def move(cnt, location):
    global min_cnt
    if location == n - 1:
        min_cnt = min(min_cnt, cnt)
        return
    value = balls[location]
    for i in range(1, value + 1):
        if in_range(location + i):
            move(cnt + 1, location + i)

move(0, 0)
if min_cnt == 1e9:
    print(-1)
else:
    print(min_cnt)
