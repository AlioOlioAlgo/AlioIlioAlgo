"""
 *packageName    : 
 * fileName       : 세 수의 합
 * author         : ipeac
 * date           : 2023-02-17
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2023-02-17        ipeac       최초 생성
 """
from collections import deque

n, g, = map(int, input().split())
ans = 0
invited = [False] * n  # 초댓장을 받았는지 여부를 저장함
groups = [set() for _ in range(g)]  # 그룹 0 1 2 3 부터 해서 각각 몇번째 사람에게 초대장을 줄수있는지 기록한다.
group_per_person = [
    [] for _ in range(n)
]
for i in range(g):
    member = list(map(int, input().split()))[1:]
    for mem in member:  # 각 그룹 마다 속하는 사람들 번호
        mem -= 1
        groups[i].add(mem)
        group_per_person[mem].append(i)

q = deque([0])  # 1번째 사람을 처음에 돌려야합니다.
invited[0] = True
while q:
    x = q.popleft()  # 0
    ans += 1
    
    # 해당 1번 등등 사람을 모든 그룹에서 지워야합니다.
    for g_num in group_per_person[x]:
        groups[g_num].remove(x)  # 모든 그룹에서 해당하는 사람 번호를 지웁니다 ( 이미 받앗기 때문)
        if len(groups[g_num]) == 1:
            take_person = list(groups[g_num])[0]
            if not invited[take_person]:
                invited[take_person] = True
                q.append(take_person)
print(ans)
