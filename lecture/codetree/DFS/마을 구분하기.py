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
import sys

sys.setrecursionlimit(10 ** 5)
peoples = []
person = 0
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

n = int(input())
graph = [
    list(map(int, input().split()))
    for _ in range(n)
]
visited = [
    [False for _ in range(n)]
    for _ in range(n)
]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def dfs(x, y):
    global person
    for xx, yy in zip(dx, dy):
        nx, ny = xx + x, yy + y
        if in_range(nx, ny) and graph[nx][ny] == 1 and visited[nx][ny] == False:
            visited[nx][ny] = True
            person += 1
            dfs(nx, ny)

for i in range(n):
    for j in range(n):
        if not visited[i][j] and graph[i][j] == 1:
            visited[i][j] = True
            person = 1
            dfs(i, j)
            peoples.append(person)
print(len(peoples))
peoples.sort()
for i in range(len(peoples)):
    print(peoples[i])
