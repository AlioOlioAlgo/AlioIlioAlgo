"""


"""

n, m = map(int, input().split())
budget = [
    int(input())
    for _ in range(n)
]

# 최솟값 ~ 합게 까지 돈을 뽑을 수 있습니다.
min_value, max_value = min(budget), sum(budget)
mid = 0
while min_value <= max_value:
    mid = (min_value + max_value) // 2
    now_value = mid  # 인출할 돈 ㅇㅇ
    draw_count = 1
    
    for i in budget:
        if now_value < i:
            now_value = mid
            draw_count += 1
        now_value -= i
    
    # 인출한 금액이 하루를 다 살수없는 경우
    if draw_count > m or mid < max(budget):
        min_value = mid + 1
    else:
        max_value = mid - 1
print(mid)
