"""
 *packageName    :
 * fileName       : 배열 추출 2
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
arr = []
for i in range(n):
    input_value = int(input())
    if input_value:
        heapq.heappush(arr, (abs(input_value), input_value,))
    
    else:
        if len(arr) == 0:
            print(0)
        else:
            print(heapq.heappop(arr)[1])
