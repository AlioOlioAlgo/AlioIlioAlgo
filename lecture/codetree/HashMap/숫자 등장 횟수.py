"""
 *packageName    : 
 * fileName       : 숫자 등장 횟수
 * author         : ipeac
 * date           : 2023-02-17
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2023-02-17        ipeac       최초 생성
"""
from collections import defaultdict

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

print(f"arr  ==> {arr}")
print(f"arr2  ==> {arr2}")
count = defaultdict(int)
for ar in arr:
    count[ar] += 1
for value in arr2:
    print(count[value], end=" ")
