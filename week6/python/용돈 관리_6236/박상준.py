import sys

input = sys.stdin.readline

N, M = map(int, input().split())
budget = [int(input()) for _ in range(N)]
l, r = min(budget), sum(budget)
while l <= r:
    m = (l + r) // 2
    now = m
    draw = 1
    
    for i in budget:
        if now < i:
            now = m
            draw += 1
        now -= i
    
    if draw > M or m < max(budget):
        l = m + 1
    else:
        r = m - 1
        k = m
print(k)
