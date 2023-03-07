"""
 *packageName    : 
 * fileName       : 11053.가장 긴 증가하는 부분 수열
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
for i in range(1, n):
    cnt = 0
    for j in range(i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[i], dp[j] + 1)
print(max(dp))
