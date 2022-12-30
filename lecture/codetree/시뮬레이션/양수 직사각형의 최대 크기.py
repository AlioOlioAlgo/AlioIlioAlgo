"""
 *packageName    :
 * fileName       : 양수 직사각형의 최대 크기
 * author         : ipeac
 * date           : 2022-12-29
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-12-29        ipeac       최초 생성
 """
n, m = map(int, input().split())
graph = [
    list(map(int, input().split()))
    for _ in range(n)
]

def check_all_plus(start_row, start_col, end_row, end_col):
    size = 0
    for i in range(start_row, end_row + 1):
        for j in range(start_col, end_col + 1):
            if graph[i][j] <= 0:
                return False, size
            else:
                size += 1
    return True, size

max_size = 0
for i in range(n):
    for j in range(m):
        for row in range(i, n):
            for col in range(j, m):
                # print("==========================================")
                # print(f"i = {i}")
                # print(f"j = {j}")
                # print(f"row = {row}")
                # print(f"col = {col}")
                check, size_return = check_all_plus(i, j, row, col)
                if check:
                    max_size = max(max_size, size_return)

print(max_size) if max_size else print(-1)
