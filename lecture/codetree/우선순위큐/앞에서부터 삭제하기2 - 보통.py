"""
 *packageName    :
 * fileName       : 앞에서부터 삭제하기2 - 보통
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
max_avg = 0
sum_value = 0
ans = []

heapq.heappush(ans, arr[n - 1])
sum_value += arr[n - 1]

for k in range(n - 2, 0, -1):
    heapq.heappush(ans, arr[k])
    sum_value += arr[k]
    
    # ans 최소힙으로 구현되어있음
    avg = (sum_value - ans[0]) / (n - k - 1)
    max_avg = max(avg, max_avg)
print(f"{max_avg:.2f}")
