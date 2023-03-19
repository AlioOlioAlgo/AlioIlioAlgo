"""
 *packageName    : 
 * fileName       : 낮은 지점들
 * author         : ipeac
 * date           : 2023-02-25
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2023-02-25        ipeac       최초 생성
"""
from collections import defaultdict

n = int(input())

count = defaultdict(int)

for i in range(n):
    a, b = map(int, input().split())
    print(f"a,b  ==> {a, b}")
    if a in count:
        if count[a] > b:
            count[a] = b
    else:
        count[a] = b
    print(f"count  ==> {count}")
ans = 0
for value in count.values():
    ans += value
print(ans)
