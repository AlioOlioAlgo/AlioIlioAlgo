"""
 *packageName    :
 * fileName       : 주사위 던지기
 * author         : ipeac
 * date           : 2023-01-17
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2023-01-17        ipeac       최초 생성
 """
n, m, r, c = map(int, input().split())
up, front, right = 1, 2, 3
graph = [
    [0 for _ in range(n)]
    for _ in range(n)
]
graph[r - 1][c - 1] = 7 - up
print(f"graph = {graph}")
direction = list(map(str, input().split()))
print(f"direction = {direction}")

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

for way in direction:
    if way == 'L':
        c -= 1
        if not in_range(r - 1, c - 1):
            c += 1
            continue
        tmp_up = up
        up = right
        right = 7 - tmp_up
    elif way == 'R':
        c += 1
        if not in_range(r - 1, c - 1):
            c -= 1
            continue
        tmp_up = up
        up = 7 - right
        right = tmp_up
    elif way == 'U':
        r -= 1
        if not in_range(r - 1, c - 1):
            r += 1
            continue
        tmp_up = up
        up = front
        front = 7 - tmp_up
    elif way == 'D':
        r += 1
        if not in_range(r - 1, c - 1):
            r -= 1
            continue
        tmp_up = up
        up = 7 - front
        front = tmp_up
    graph[r - 1][c - 1] = 7 - up
ans = 0
for num in graph:
    ans += sum(num)
print(ans)
