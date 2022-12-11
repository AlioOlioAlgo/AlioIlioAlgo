"""
 *packageName    :
 * fileName       : 박상준3
 * author         : ipeac
 * date           : 2022-12-11
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-12-11        ipeac       최초 생성
 """
n, m = map(int, input().split())  # n  세로 크기   m 가로 크기

def bitmask():
    global max_ans
    # 비트마스크로 2*(N*M)의 경우의 수를 따진다.
    for i in range(1 << n * m):
        total = 0
        # 가로 합 계산
        for row in range(n):
            row_sum = 0
            for col in range(m):
                # idx는 이차원 배열을 (비트마스킹) 일렬로 늘렸을 때 인덱스가 어디인지 의미
                idx = row * m + col
                # 가로 일때
                if i & (1 << idx) != 0:
                    row_sum = row_sum * 10 + arr[row][col]
                # 세로일 떄 앞에서 나온 수를 total에 더하고, row sum
                else:
                    total += row_sum
                    row_sum = 0
            total += row_sum
        for col in range(m):
            col_sum = 0
            for row in range(n):
                idx = row * m + col
                
                if i & (1 << idx) == 0:
                    col_sum = col_sum * 10 + arr[row][col]
                
                else:
                    total += col_sum
                    col_sum = 0
            total += col_sum
        max_ans = max(max_ans, total)

arr = [
    list(map(int, input()))
    for _ in range(n)
]

max_ans = 0

bitmask()
print(max_ans)
