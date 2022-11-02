"""
 *packageName    : 
 * fileName       : 박상준
 * author         : ipeac
 * date           : 2022-10-29
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-10-29        ipeac       최초 생성
 """
# n = int(input())
# scv = list(map(int, input().split()))
# dp = [i for i in range(n)]
# print(f"n = {n}")
# print(f"scv = {scv}")
# print(f"dp = {dp}")
from collections import deque
from itertools import permutations

n = 3
scv = [4, 10, 12]
# scv = sorted(list(map(int, stdin.readline().split())) + (3 - n) * [0])
# print(f"scv = {scv}")
ONE, TWO, THREE, CNT = 0, 1, 2, 3

def bfs():
    q = deque([[*scv, 0]])  # scv 현황과 cnt 을 디큐에 저장
    while q:
        cur_state = q.popleft()  # 현재 상태
        # **정렬된 상태에서** 체력이 큰 SCV의 체력이 없다면 종료
        if cur_state[THREE] == 0:
            return cur_state[CNT]
        # 공격 가능한 경우의 수만큼 큐에 추가한다.
        for case in attack_case:
            next_scv = [0] * 3
            # visited 에 방문 여부를 체크하기 위해 0보다 작은 경우 0으로 변환
            for i in range(3):
                next_scv[i] = cur_state[i] - case[i] if cur_state[i] - case[i] > 0 else 0
            # 정렬된 상태로 큐에 추가
            next_scv.sort()
            
            if not visited[next_scv[ONE]][next_scv[TWO]][next_scv[THREE]]:
                visited[next_scv[ONE]][next_scv[TWO]][next_scv[THREE]] = 1
                q.append([*next_scv, cur_state[CNT] + 1])
    pass

attack_case = list(permutations([9, 3, 1], 3))
visited = [[[0] * 61 for _ in range(61)] for _ in range(61)]
# 3차원 배열 visited


print(bfs())
