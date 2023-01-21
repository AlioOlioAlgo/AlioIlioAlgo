"""
 *packageName    :
 * fileName       : 핀볼게임
 * author         : ipeac
 * date           : 2023-01-18
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2023-01-18        ipeac       최초 생성
 """
n = int(input())
graph = [
    list(map(int, input().split()))
    for _ in range(n)
]

print(f"graph = {graph}")

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

#  동 서 남 북
# 위로 들어가기.


def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def way_one():
    global way
    if way == 2:
        way = 1
    elif way == 0:
        way = 3
    elif way == 1:
        way = 2
    else:
        way = 0

def way_two():
    global way
    if way == 2:
        way = 0
    elif way == 0:
        way = 2
    elif way == 1:
        way = 3
    else:
        way = 1

max_cnt = 0

for y in range(n):
    cnt = 0
    # 남쪽으로
    way = 2
    x = 0
    while in_range(x, y):
        if graph[x][y] == 1:
            way_one()
        elif graph[x][y] == 2:
            way_two()
        x, y = x + dx[way], y + dy[way]
        cnt += 1
    else:
        max_cnt = max(max_cnt, cnt)
    print(f"max_cnt = {max_cnt}")

for y in range(n):
    cnt = 0
    # 북쪽
    way = 3
    x = n - 1
    while in_range(x, y):
        if graph[x][y] == 1:
            way_one()
        elif graph[x][y] == 2:
            way_two()
        x, y = x + dx[way], y + dy[way]
        cnt += 1
    else:
        max_cnt = max(max_cnt, cnt)

for x in range(n):
    cnt = 0
    # 동쪽
    way = 0
    y = 0
    while in_range(x, y):
        if graph[x][y] == 1:
            way_one()
        elif graph[x][y] == 2:
            way_two()
        x, y = x + dx[way], y + dy[way]
        cnt += 1
    else:
        max_cnt = max(max_cnt, cnt)

for x in range(n):
    cnt = 0
    # 서쪽
    way = 1
    y = n - 1
    while in_range(x, y):
        if graph[x][y] == 1:
            way_one()
        elif graph[x][y] == 2:
            way_two()
        x, y = x + dx[way], y + dy[way]
        cnt += 1
    else:
        max_cnt = max(max_cnt, cnt)
print(max_cnt + 1)
