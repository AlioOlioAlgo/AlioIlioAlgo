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

# print(f"n = {n}")
# print(f"node = {node}")
# print(f"tree = {tree}")
# print(f"del_node = {del_node}")
# n = 5
# node = [-1, 0, 0, 1, 1]
# del_node = 1

# 노드 2를 지우면 아래의 모든 정점이 사라진다.
def dfs(del_num):
    # 노드의 해당 부분을 임의의 -2 로 설정한다.
    node[del_num] = -2  # node [2] =-2 로 설정됨.
    for i in range(len(node)):
        # 부모 번호와 노드가 가리키는 부모 번호가 동일한 경우
        if node[i] == del_num:
            # 해당 노드를 부모로 둔 친구들까지 -2 로 만들어줄 수 있도록 재귀
            dfs(i)

dfs(del_node)  # 2
# print(f"node = {node}")  # print('node = [-1, -2, 0, -2, -2]')
# -1 처리하면 안됨?
# => 부모가 없는 노드가 리프노드는 아님.. 루트노드임.ㅇㅇ.
# -2 처리해서 리프 노드라는 걸 알려줘야함 ㅇㅇ
#
# 이제 노드에서 -2 는 제거된 친구니까 제외
# node index에 해당하는 값이 node 에 존재하지 않다면 유일한 리프노드 =>
# 아무도 이 정점을 부모로 여기고 있지 않다는 의미이다.
ans = 0
for idx in range(len(node)):
    if node[idx] != -2 and idx not in node:
        ans += 1
        pass
print(ans)
