"""
 *packageName    :
 * fileName       : Queens
 * author         : ipeac
 * date           : 2022-12-03
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-12-03        ipeac       최초 생성
 """
n, m = map(int, input().split())  # n  n* n 크기의 판이 존재한다.

remaining_queen = n - m

chess = [
    list(map(str, input().split()))
    for _ in range(n)
]

col = [0] * (n + 1)

for i in range(n):
    for j in range(n):
        # 해당 row 의 q 가 존재한다면 col을 기록한다.
        if chess[i][j] == 'Q':
            #  i가 row 에 해당 값이 column q 위치
            col[i] = j

def dfs(col, depth):
    n = len(col) - 1
    if check_queen(col, depth):
        if depth == n:
            print(col[1:])
        else:
            for j
        pass

dfs(col, 0)
