"""
 *packageName    :
 * fileName       : 최고의 33위치
 * author         : ipeac
 * date           : 2022-12-27
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-12-27        ipeac       최초 생성
 """
n = int(input())  # n  격자의 크기
graph = [
    list(map(int, input().split()))
    for _ in range(n)
]

def line_three(row, col):
    cnt = 0
    for i in range(row, row + 3):
        for j in range(col, col + 3):
            if graph[i][j]:
                cnt += 1
    return cnt

ans = 0
for i in range(n - 2):
    for j in range(n - 2):
        ans = max(ans, line_three(i, j))  # 3 3 격자안의 최대 동전
print(ans)
