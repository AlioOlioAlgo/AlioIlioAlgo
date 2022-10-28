"""
 *packageName    : 
 * fileName       : 박상주
 * author         : ipeac
 * date           : 2022-10-28
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-10-28        ipeac       최초 생성
 """
# m : 폐업시키지 않을 치킨집 나머지 집은 폐업임
# 어떻게 고르면 도시의 치킨 거리가 가장 적게 될지?

# n, m = map(int, input().split())
# graph = [
#     list(map(int, input().split()))
#     for _ in range(n)
# ]
#
# print(f"n,m = {n, m}")
# print(f"graph = {graph}")
n, m = (5, 1)
graph = [[1, 2, 0, 2, 1], [1, 2, 0, 2, 1], [1, 2, 0, 2, 1], [1, 2, 0, 2, 1], [1, 2, 0, 2, 1]]
home = []
chicken = []

# 브루트포스 # 백트킹킹
def dfs():
    pass

for i in range(n):
    for j in range(n):
