"""
 *packageName    : 
 * fileName       : 점 빼기
 * author         : ipeac
 * date           : 2023-02-23
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2023-02-23        ipeac       최초 생성
"""
import bisect

n, m = map(int, input().split())
point_location = [
    tuple(map(int, input().split()))
    for _ in range(n)
]
point_location.sort(key=lambda x: (x[0], x[1]))
for i in range(m):
    question = int(input())
    index = bisect.bisect_right(point_location, (question, -1))
    
    if index == len(point_location):
        print(-1, -1)
        continue
    else:
        print(point_location[index][0], point_location[index][1])
        point_location.pop(index)
