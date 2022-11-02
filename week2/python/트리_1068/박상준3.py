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
n = int(input())
parent = list(map(int, input().split()))
delete = int(input())

def dfs(delete):  # 2    value 0
    parent[delete] = -2
    for i in range(len(parent)):
        # print(f"parent = {parent[i]}")
        # print(f"delete = {delete}")
        if parent[i] == delete:  #
            dfs(i)

dfs(delete)

# print(parent)
cnt = 0
for i in range(len(parent)):
    if parent[i] != -2 and i not in parent:
        cnt += 1
print(cnt)
