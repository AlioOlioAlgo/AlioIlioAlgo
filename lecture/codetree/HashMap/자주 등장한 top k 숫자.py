"""
 *packageName    : 
 * fileName       : 자주 등장한 top k 숫자
 * author         : ipeac
 * date           : 2023-02-18
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2023-02-18        ipeac       최초 생성
"""
from collections import defaultdict

n, k = map(int, input().split())
arr = list(map(int, input().split()))

count = defaultdict(int)

for value in arr:
    count[value] += 1
sorted_dict = sorted(count.items(), key=lambda x: (-x[1], -x[0]))

for i in range(k):
    print(sorted_dict[i][0], end=" ")
