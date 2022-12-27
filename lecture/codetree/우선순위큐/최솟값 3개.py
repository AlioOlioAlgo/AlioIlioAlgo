"""
 *packageName    :
 * fileName       : 최솟값 3개
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
ans = []
for ar in arr:
    heapq.heappush(ans, ar)
    # print(f"ans = {ans}")
    if len(ans) < 3:
        print(-1)
    else:
        first = heapq.heappop(ans)
        second = heapq.heappop(ans)
        third = heapq.heappop(ans)
        prod_value = first * second * third
        heapq.heappush(ans, first)
        heapq.heappush(ans, second)
        heapq.heappush(ans, third)
        print(prod_value)
