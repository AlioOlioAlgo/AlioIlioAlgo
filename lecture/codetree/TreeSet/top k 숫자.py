"""
 *packageName    : 
 * fileName       : top k 숫자
 * author         : ipeac
 * date           : 2023-02-22
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2023-02-22        ipeac       최초 생성
 """
from sortedcontainers import SortedSet

n, k = map(int, input().split())
arr = set(map(int, input().split()))

tree_set = SortedSet()
for x in arr:
    tree_set.add(-x)
print(f"tree_set  ==> {tree_set}")
for i in range(k):
    print(-tree_set[i], end=" ")
