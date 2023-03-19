"""
 *packageName    :
 * fileName       : 마지막으로 남은 숫자
 * author         : ipeac
 * date           : 2022-12-27
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-12-27        ipeac       최초 생성
 """
import heapq

n = int(input())
arr = list(map(int, input().split()))
arr = [-num for num in arr]
heapq.heapify(arr)
while len(arr) >= 2:
    big_one = -heapq.heappop(arr)
    big_second = - heapq.heappop(arr)
    if big_one == big_second:
        continue
    diff = abs(big_one - big_second)
    heapq.heappush(arr, -diff)
if len(arr):
    print(-arr[0])
else:
    print(-1)
