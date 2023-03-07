"""
 *packageName    : 
 * fileName       : 쉬운 계단 수
 * author         : ipeac
 * date           : 2023-03-04
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2023-03-04        ipeac       최초 생성
"""
n = int(input())  # 입력받은 자리수

# dp[i][j]는 i자리 수에서 j로 끝나는 계단 수의 개수
dp = [[0] * 10 for _ in range(n + 1)]

# 초기값 설정
for i in range(1, 10):
    dp[1][i] = 1

# 점화식을 이용해 dp 테이블 갱신
for i in range(2, n + 1):
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i - 1][j + 1]
        elif j == 9:
            dp[i][j] = dp[i - 1][j - 1]
        else:
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j + 1]

# n자리 계단 수의 총 개수는 dp[n]의 모든 원소의 합과 같음
print(sum(dp[n]) % 1000000000)
