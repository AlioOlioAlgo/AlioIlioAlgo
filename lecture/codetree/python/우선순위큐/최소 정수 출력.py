"""
 *packageName    :
 * fileName       : 최소 정수 출력
 * author         : ipeac
 * date           : 2022-12-26
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-12-26        ipeac       최초 생성
 """
import heapq

n = int(input())
arr = []
for _ in range(n):
    input_int = int(input())
    if not input_int:
        if not len(arr):
            print(0)
        else:
            print(heapq.heappop(arr))
    else:
        heapq.heappush(arr, input_int)
