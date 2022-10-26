"""
 *packageName    : 
 * fileName       : 박상준
 * author         : ipeac
 * date           : 2022-10-26
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-10-26        ipeac       최초 생성
 """
# n = int(input())
# parents = list(map(int, input().split()))  # 부모가 없으면 -1
# delete_node = int(input())
# print(f"n = {n}")
# print(f"parents = {parents}")
# print(f"delete_node = {delete_node}")

n = 5
parents = [-1, 0, 0, 1, 1]
delete_node = 0

def dfs(del_num):
    # 부모를 삭제할 -2 로 임의 설정
    parents[del_num] = -2
    print(f"parents = {parents}")
    # 루프
    for i in range(n):
        # 삭제된 부모의 인덱스 번호를 가진 parents 가 보이면
        if del_num == parents[i]:
            print(i)
            # 똑같이 해당 번호를 -2 로 임의로 설정하고 -> 이후 i 를 부모로 둔 자식을 찾아서 다 -2 로 변경
            dfs(i)

dfs(delete_node)

count = 0

# 부모 리스트 순회
for i in range(len(parents)):
    # -2 가 아니며! 해당 인덱스가 parents 에서 안보인다면 리프 노드이다.
    if parents[i] != -2 and i not in parents:
        count += 1
print(count)
