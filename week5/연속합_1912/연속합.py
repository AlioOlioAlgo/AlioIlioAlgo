"""

 *packageName    :
 * fileName       : 박상준
 * author         : ipeac
 * date           : 2022-12-07
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-12-07        ipeac       최초 생성
 """
n = int(input())
number_list = list(map(int, input().split()))

total = number_list[0]
dp = [0] * n
dp[0] = number_list[0]
for idx in range(1, n):
    # print("=====================number_list[idx]=====================")
    dp[idx] = max(number_list[idx], dp[idx - 1] + number_list[idx])
    # print(number_list[idx])
    # print(dp[idx - 1] + number_list[idx])
    # print(f"dp = {dp}")

print(max(dp))
