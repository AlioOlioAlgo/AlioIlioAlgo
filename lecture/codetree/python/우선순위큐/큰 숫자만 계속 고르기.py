"""
 *packageName    :
 * fileName       : 큰 숫자만 계속 고르기
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
number = list(map(int, input().split()))
number = [-num for num in number]
heapq.heapify(number)
for _ in range(m):
    heapq.heappush(number, heapq.heappop(number) + 1)
print(-heapq.heappop(number))
