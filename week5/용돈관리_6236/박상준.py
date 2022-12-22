"""
 *packageName    :
 * fileName       : 박상준
 * author         : ipeac
 * date           : 2022-12-22
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-12-22        ipeac       최초 생성
 """
N, M = map(int, input().split())  # N : 일 동안 사용할 금액 M : 번만 통장에서 돈 인출
draw = [
    int(input())
    for _ in range(N)
]  # N일 동안 빼낼 돈
global_min = int(1e9)
min_value, sum_value, = min(draw), sum(draw),
ans = 0
while min_value <= sum_value:
    mid = (min_value + sum_value) // 2
    now_money = mid
    count = 1
    for i in draw:
        if now_money < i:
            now_money = mid
            count += 1
        now_money -= i
    if count > M or mid < max(draw):
        min_value = mid + 1
    else:
        sum_value = mid - 1
        ans = mid
print(ans)
