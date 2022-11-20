"""
 *packageName    :
 * fileName       : 박상준
 * author         : ipeac
 * date           : 2022-11-20
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-11-20        ipeac       최초 생성
 """
import heapq

n = int(input())
case = []
ans = []
for i in range(n):
    deadline, cup = map(int, input().split())
    case.append([deadline, cup])
case.sort(key=lambda x: x[0])

print(f"case = {case}")
day = 0
for cas in case:
    heapq.heappush(ans, cas[1])
    if cas[0]
