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

col = [0] * n
for i in range(n):
    for j in range(n):
        # 해당 row 의 q 가 존재한다면 col을 기록한다.
        if chess[i][j] == 'Q':
            print(f"i,j = {i, j}")
            if col[i]:  # 한 행에 Q 여러개 있는 예제면 걍 false 임
                print('false')
                exit()
            #  i가 row 에 해당 값이 column q 위치
            col[i] = j + 1
print(f"col = {col}")

def check(col, depth):
    # 열체크 + 대각 체크
    # 결국 모든 행을 전부 체크해야합니다. 뒷행도 존재하기에
    for i in range(depth):
        if col[i] == col[depth] or abs(col[i] - col[depth]) == abs(i - depth):  # 겹치면 false 처리
            return False
    
    for i in range(depth + 1, n):
        if col[i] == col[depth] or abs(col[i] - col[depth]) == abs(i - depth):  # 겹치면 false 처리
            return False
    return True

def dfs(col, depth):
    print(f"col = {col}")
    print(f"depth = {depth}")
    if check(col, depth):
        if depth == n:
            print('true')
            return True
        else:
            for j in range(n):
                col[depth + 1] = j
                dfs(col, depth + 1)

dfs(col, 0)
