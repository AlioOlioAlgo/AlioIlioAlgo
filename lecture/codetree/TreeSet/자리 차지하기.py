"""
 *packageName    : 
 * fileName       : 자리 차지하기
 * author         : ipeac
 * date           : 2023-02-22
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2023-02-22        ipeac       최초 생성
"""
import bisect

n, m = map(int, input().split())
seats = list(map(int, input().split()))

arr = [i for i in range(1, m + 1)]

answer = 0

for i in range(n):
    index = bisect.bisect_right(arr, seats[i])
    
    if index != 0:
        index -= 1
        arr.remove(arr[index])
        
        # 답을 갱신합니다.
        answer += 1
    else:
        break
print(answer)
