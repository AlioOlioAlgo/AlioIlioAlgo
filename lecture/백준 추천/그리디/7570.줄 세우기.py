"""
 *packageName    : 
 * fileName       : 7570.줄 세우기
 * author         : ipeac
 * date           : 2023-03-10
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2023-03-10        ipeac       최초 생성
 """
n = int(input())
num = list(map(int, input().split()))
dp = [0] * (n + 1)

for i in range(n):
    dp[num[i]] = dp[num[i] - 1] + 1
print(n - max(dp))
