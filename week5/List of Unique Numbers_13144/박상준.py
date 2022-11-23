"""
 *packageName    :
 * fileName       : 박상준
 * author         : ipeac
 * date           : 2022-11-23
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-11-23        ipeac       최초 생성
 """
"""
5
1 1 1 1 1

5

5
1 2 3 4 5

15

5
1 2 3 1 2

12
"""

n = int(input())
# n = 100000
# arr = [i for i in range(1, 100001)]
arr = list(map(int, input().split()))
start = 0
end = 0
check = [0] * 100001
ans = 0
while start <= n - 1:
    if end == n:
        end = n - 1
    # print("==========================================")
    if not check[arr[end]]:  # 방문 x
        # print(f"start = {start}")
        # print(f"end = {end}")
        # print(f"arr[end] = {arr[end]}")
        ans += 1
        check[arr[end]] = 1
        end += 1
    else:  # 방문 O
        # print(f"start = {start}")
        # print(f"end = {end}")
        # print("방문 O")
        check = [0] * 100001
        start += 1
        end = start
        # print(f"start = {start}")
        # print(f"end = {end}")

print(ans)
