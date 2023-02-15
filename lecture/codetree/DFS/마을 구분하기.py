"""
 *packageName    : 
 * fileName       : 마을 구분하기
 * author         : ipeac
 * date           : 2023-02-15
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2023-02-15        ipeac       최초 생성
 """
town_cnt = 0
people_cnt = 0

n = int(input())
graph = [
    list(map(int, input().split()))
    for _ in range(n)
]
visited = [

]

def dfs(x, y):
    pass

for i in range(n):
    for j in range(n):
        dfs(i, j)
