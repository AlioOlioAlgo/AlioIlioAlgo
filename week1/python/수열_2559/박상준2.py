"""
 *packageName    : 
 * fileName       : 박상준2
 * author         : ipeac
 * date           : 2022-10-27
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-10-27        ipeac       최초 생성
 """
n, k = map(int, input().split())
temp = list(map(int, input().split()))
# print(f"n,k = {n, k}")
# print(f"temp = {temp}")
# n, k = (10, 2)
# temp = [3, -2, -4, -9, 0, 3, 7, 13, 8, -3]
max_value = -1e9
start = 0
curr_value = 0

for end, value in enumerate(temp):
    curr_value += value
    if end - start + 1 == k:
        max_value = max(max_value, curr_value)
        curr_value -= temp[start]
        start += 1
print(max_value)
