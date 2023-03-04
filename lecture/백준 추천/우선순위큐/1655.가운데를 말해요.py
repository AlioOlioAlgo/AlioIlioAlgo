"""
 *packageName    : 
 * fileName       : 1655.가운데를 말해요
 * author         : ipeac
 * date           : 2023-03-04
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2023-03-04        ipeac       최초 생성
"""
import heapq

n = int(input())
left = []  # 작은 수를 담을 최대 힙
right = []  # 큰 수를 담을 최소 힙
result = []

for i in range(n):
    print("======================================================")
    num = int(input())
    
    # left에 먼저 원소를 넣고, left의 최대값을 right의 최소값과 비교하여 조건에 맞게 swap
    if len(left) <= len(right):
        heapq.heappush(left, -num)
    else:
        heapq.heappush(right, num)
    
    print(f"left  ==> {left}")
    print(f"right  ==> {right}")
    
    if right and -left[0] > right[0]:
        heapq.heappush(right, -heapq.heappop(left))
        heapq.heappush(left, -heapq.heappop(right))
    
    # 중앙값을 result 리스트에 추가
    result.append(-left[0])

# 결과 출력
for res in result:
    print(res)
