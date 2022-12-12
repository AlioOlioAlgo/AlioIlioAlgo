"""
 *packageName    :
 * fileName       : 순회강연3
 * author         : ipeac
 * date           : 2022-12-06
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-12-06        ipeac       최초 생성
 """
import heapq

n = int(input())
lecture = [
    list(map(int, input().split()))
    for _ in range(n)
]
lecture.sort(key=lambda x: (x[1], -x[0]))
print(f"lecture = {lecture}")

ans = []
for lec in lecture:
    day = lec[1]
    value = lec[0]
    heapq.heappush(ans, value)  # 최소힙 푸쉬 #최소값 유지를 위함
    
    if day < len(ans):  # 해당 날짜가 수용할 수 있는 값보다 많이 들어갔으니 제일 작은 값을 빼줘야지
        heapq.heappop(ans)
print(sum(ans))
