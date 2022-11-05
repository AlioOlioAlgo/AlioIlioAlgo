"""
 *packageName    :
 * fileName       : 박상준3
 * author         : ipeac
 * date           : 2022-11-02
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-11-02        ipeac       최초 생성
 """
n = 5
parent = [-1, 0, 0, 1, 1]
delete = 1

def dfs(delete):
    parent[delete] = -2
    for i in range(len(parent)):
        if parent[i] == delete:
            dfs(i)

dfs(delete)

cnt = 0
for i in range(len(parent)):
    if parent[i] != -2 and i not in parent:
        cnt += 1
print(cnt)
