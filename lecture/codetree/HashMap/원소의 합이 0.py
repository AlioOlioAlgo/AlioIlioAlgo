"""
 *packageName    : 
 * fileName       : 원소의 합이 0
 * author         : ipeac
 * date           : 2023-02-18
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2023-02-18        ipeac       최초 생성
"""
from collections import defaultdict

n = int(input())

a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
d = list(map(int, input().split()))

count_ab = defaultdict(int)
ans = 0
for i in range(n):
    for j in range(n):
        total = a[i] + b[j]
        count_ab[total] += 1
print(f"count  ==> {count_ab}")
for i in range(n):
    for j in range(n):
        total = c[i] + d[j]
        if -total in count_ab:
            ans += count_ab[-total]
print(ans)
