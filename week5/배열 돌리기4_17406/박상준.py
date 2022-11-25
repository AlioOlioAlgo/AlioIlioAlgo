"""
 *packageName    :
 * fileName       : 박상준
 * author         : ipeac
 * date           : 2022-11-25
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-11-25        ipeac       최초 생성
 """
from copy import deepcopy
from itertools import permutations

dx, dy = [0, 1, 0, -1], [1, 0, -1, 0],

n, m, k = map(int, input().split())  # n  배열의 세로  m 배열의 가로   k 회전 배열의 수
graph = [
    list(map(int, input().split()))
    for _ in range(n)
]
print(f"graph = {graph}")
rotate_arr = [
    list(map(int, input().split()))
    for _ in range(k)
]
print(f"rotate_arr = {rotate_arr}")

min_value = int(1e9)
for rotate_permutation in permutations(rotate_arr, k):
    print(f"rotate_permutation = {rotate_permutation}")
    a = deepcopy(graph)
    for r, c, s in rotate_permutation:
        print("==========================================")
        for i in range(s):
            top = [r - s + i - 1, c - s + i - 1]
            botton = [r + s - i - 1, c + s - i - 1]
            nx, ny = top
            prev = a[nx][ny]
            
            for d in range(4):
                while True:
                    nx, ny = nx + dx[d], ny + dy[d]
                    if not top[0] <= nx <= botton[0] or not top[1] <= ny <= botton[1]:
                        nx, ny = nx - dx[d], ny - dy[d]
                        break
                    prev, a[nx][ny] = a[nx][ny], prev
    for row in a:
        min_value = min(min_value, sum(row))
print(min_value)
