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
from sortedcontainers import SortedSet

# 변수 선언 및 입력:
n, m = tuple(map(int, input().split()))
arr = list(map(int, input().split()))

# 1번부터 m번까지 전부 비어져 있으므로
# 빈 위치를 treeset으로 관리합니다.
seats = SortedSet(range(1, m + 1))

# 답을 구해줍니다.
ans = 0

# 순서대로 앉혀봅니다.
# 최선의 자리 선택은
# ai보다 같거나 작은 최대 위치에 자리배치를 하는 것입니다.
for elem in arr:
    # ai보다 큰 최초의 위치를 먼저 찾습니다.
    idx = seats.bisect_right(elem)
    
    # 만약 큰 최초의 위치가
    # 첫 번째 위치가 아니라면,
    # 바로 전 위치가
    # ai보다 같거나 작은 최대 위치가 구해지므로,
    # 해당 위치에 사람을 앉혀줍니다.
    if idx != 0:
        idx -= 1
        seats.remove(seats[idx])
        
        # 답을 갱신해줍니다.
        ans += 1
    else:
        break

print(ans)
