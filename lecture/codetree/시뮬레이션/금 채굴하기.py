"""
 *packageName    :
 * fileName       : 금 채굴하기
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
    [0 for _ in range(n + 2)]
    for _ in range(n + 2)
]

for i in range(n):
    arr = list(map(int, input().split()))
    for j in range(n):
        if arr[j] == 1:
            graph[i + 1][j + 1] = 1
print(f"graph = {graph}")
# 1번 인덱스부터 돌기 시작합니다.
