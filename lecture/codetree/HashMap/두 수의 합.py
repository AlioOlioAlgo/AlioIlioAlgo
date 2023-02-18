"""
 *packageName    : 
 * fileName       : 두 수의 합
 * author         : ipeac
 * date           : 2023-02-17
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2023-02-17        ipeac       최초 생성
 """
from collections import defaultdict

n, k = map(int, input().split())
arr = list(map(int, input().split()))
count = defaultdict(int)

ans = 0

for i in range(n):
    diff = k - arr[i]
    
    if diff in count:
        ans += count[diff]
    count[arr[i]] += 1
print(ans)
