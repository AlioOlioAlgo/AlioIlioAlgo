"""
 *packageName    :
 * fileName       : 가장 가까운 점
 * author         : ipeac
 * date           : 2022-12-26
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-12-26        ipeac       최초 생성
 """
import heapq

n, m = map(int, input().split())
ans = []
for _ in range(n):
    x, y = map(int, input().split())
    heapq.heappush(ans, (abs(x) + abs(y), x, y))
for _ in range(m):
    # print(f"ans = {ans}")
    diff, x, y = heapq.heappop(ans)
    heapq.heappush(ans, (abs(x + 2) + abs(y + 2), x + 2, y + 2))
diff, x, y = heapq.heappop(ans)
print(x, y)
