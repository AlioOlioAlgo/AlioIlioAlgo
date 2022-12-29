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
for i in range(n):
    for j in range(m):
        for row in range(i, n):
            for col in range(j, m):
                print("==========================================")
                print(f"i = {i}")
                print(f"j = {j}")
                print(f"row = {row}")
                print(f"col = {col}")
