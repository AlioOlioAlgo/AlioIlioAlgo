"""
 *packageName    :
 * fileName       : 정원 입장은 선착순
 * author         : ipeac
 * date           : 2022-12-27
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-12-27        ipeac       최초 생성
 """
import heapq
import sys

n = int(input())
cand = []
pq = []
for i in range(n):
    time, waiting, = tuple(map(int, input().split()))
    cand.append((time, i + 1, waiting))
cand.append((sys.maxsize, n + 1, 0))

cand.sort()
print(f"cand = {cand}")

exit_time = 0
ans = 0
for time, num, waiting in cand:
    while time >= exit_time and pq:  # 뒷 후보군이 도착하지 않은 시간대인데 pq 에 웨이팅이 있으면 다 소진해줘야함
        # 기다리는 사람중에 가장 우선순위가 높은 사람이 누군지 체크 .. 일단 번호표 기준으로 비교해야합니다.
        _num, _time, _waiting = heapq.heappop(pq)
        # 해당 사람이 얼마나 기다렸는지 계산한다.
        ans = max(ans, exit_time - _time)
        
        # 연속해서 일어났기에 정원 퇴장 시간은 그 전사람이 끝난 시간 + waiting 시간
        exit_time += waiting
    
    if time >= exit_time:
        exit_time = time + waiting
    else:  # 웨이팅에 등록해준다.
        heapq.heappush(pq, (num, time, waiting))
print(ans)
