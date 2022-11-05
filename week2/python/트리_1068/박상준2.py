"""
 *packageName    :
 * fileName       : 박상준2
 * author         : ipeac
 * date           : 2022-10-29
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-10-29        ipeac       최초 생성
 """
n = int(input())
node = list(map(int, input().split()))

del_node = int(input())

# 노드 2를 지우면 아래의 모든 정점이 사라진다.
def dfs(del_num):
    # 노드의 해당 부분을 임의의 -2 로 설정한다.
    node[del_num] = -2  # node [2] =-2 로 설정됨.
    for i in range(len(node)):
        # 부모 번호와 노드가 가리키는 부모 번호가 동일한 경우
        if node[i] == del_num:
            # 해당 노드를 부모로 둔 친구들까지 -2 로 만들어줄 수 있도록 재귀
            dfs(i)

# [-1 , -2 ,0 ,-2 ,-2]
dfs(del_node)  # 2
ans = 0
# 리프노드를 판별 1) 해당하는 노드의 번호가 -2 인 경우는 일반 배제 (이미 지워진 노드이기 때문에)
# 2) 해당하는 노드의 번호
for idx in range(len(node)):
    if node[idx] != -2 and idx not in node:
        ans += 1
print(ans)
