"""
 *packageName    : 
 * fileName       : 초대장과 번호표
 * author         : ipeac
 * date           : 2023-02-20
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2023-02-20        ipeac       최초 생성
"""
from collections import deque

n, g = map(int, input().split())

invited = [False] * (n)
groups = [set() for _ in range(g)]  # 각 그룹마다 초대장을 받지 못한 사람들을 관리해줍니다.
print(f"groups  ==> {groups}")
people_groups = [[] for _ in range(n)]  # 각 사람이 어떤 그룹에 속하는지를 관리해줍니다.

q = deque()
ans = 0

for i in range(g):
    group = list(map(int, input().split()))
    k = group[0]
    members = group[1:]
    for mem in members:
        mem -= 1
        groups[i].add(mem)
        people_groups[mem].append(i)
print(f"groups  ==> {groups}")
print(f"people_groups  ==> {people_groups}")
q.append(0)
invited[0] = True
while q:
    x = q.popleft()
    ans += 1
    
    # x가 들어있는 그룹에서 x를 지웁니다.
    # hashset에는 그룹에서 초대받지 않은 인원만을 남깁니다.
    for g_num in people_groups[x]:
        # 해당 그룹에서 x를 지웁니다.
        groups[g_num].remove(x)
        # 초대받지 않은 인원이 한명밖에 없다면 초대한다.
        if len(groups[g_num]) == 1:
            p_num = list(groups[g_num])[0]
            if not invited[p_num]:
                invited[p_num] = True
                q.append(p_num)
print(ans)
