"""
 *packageName    : 
 * fileName       : 13335.트럭
 * author         : ipeac
 * date           : 2023-03-16
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2023-03-16        ipeac       최초 생성
"""
from collections import deque

n, w, l = map(int, input().split())  # n 다리를 건너는 트럭의 수 | w 다리의 길이 | L 다리의 최대 하중
arr = list(map(int, input().split()))  # i번째 트럭의 무게
q = deque()
ans = 0
current_weight = 0
idx = 0

while arr:
    if q and q[0][1] == w:  # 다리를 건넌 트럭을 제거합니다.
        current_weight -= q[0][0]
        q.popleft()
    
    if current_weight + arr[0] <= l:  # 다리에 새 트럭을 올립니다.
        truck = arr.pop(0)
        q.append((truck, 0))
        current_weight += truck
    
    for i in range(len(q)):  # 다리에 있던 시간을 +1 합니다.
        q[i] = (q[i][0], q[i][1] + 1)
    
    ans += 1

ans += w  # 마지막 트럭이 다리를 건너는 시간 추가함
print(ans)
