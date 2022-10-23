"""
 *packageName    : 
 * fileName       : 박상준
 * author         : ipeac
 * date           : 2022-10-23
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-10-23        ipeac       최초 생성
 """
from collections import Counter

n, c = map(int, input().split())
# print(f"n, c = {n, c}")
integers = list(map(int, input().split()))
# print(f"integers = {integers}")

# n, c = (9, 77)
# integers = [11, 33, 11, 77, 54, 11, 25, 25, 33]
items = Counter(integers).most_common(c)
print(f"items = {items}")

for item in items:
    for _ in range(item[1]):
        print(item[0], end=" ")
