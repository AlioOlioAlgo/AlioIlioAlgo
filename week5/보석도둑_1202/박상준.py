"""
 *packageName    :
 * fileName       : 박상준
 * author         : ipeac
 * date           : 2022-11-21
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-11-21        ipeac       최초 생성
 """
import heapq
import sys
import time

def Solution(jew_list, max_weight_list):
    max_weight_list.sort()
    jew_list.sort()
    res = 0
    temp = []
    
    for bag in max_weight_list:
        while jew_list and bag >= jew_list[0][0]:
            heapq.heappush(temp, -jew_list[0][1])
            heapq.heappop(jew_list)
        
        if temp:
            res += heapq.heappop(temp)
        elif not jew_list:
            break
    print(-res)

start = time.time()
n, k = map(int, sys.stdin.readline().split())

jew_list = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
max_weight_list = [int(sys.stdin.readline()) for _ in range(k)]
Solution(jew_list, max_weight_list)
end = time.time()
print(f"{end - start:.5f}")
