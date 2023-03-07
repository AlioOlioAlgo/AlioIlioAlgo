"""
 *packageName    : 
 * fileName       : 11055.가장 큰 증가하는 부분 수열
 * author         : ipeac
 * date           : 2023-03-07
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2023-03-07        ipeac       최초 생성
"""
n = int(input())
arr = list(map(int, input().split()))
dp = [1] * n
dp[0] = arr[0]
for i in range(1, n):
    for j in range(i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[i], arr[i] + dp[j])
        else:
            dp[i] = max(dp[i], arr[i])

print(max(dp))
