"""
 *packageName    :
 * fileName       : 박상준
 * author         : ipeac
 * date           : 2022-11-16
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-11-16        ipeac       최초 생성
 """
import heapq

n = int(input())
list_a = []
for i in range(n):
    p, d = map(int, input().split())
    list_a.append([p, d])
list_a.sort(key=lambda x: x[1])
# print(f"list_a = {list_a}")
ans = []

for value in list_a:
    # print("==========================================")
    day = value[1]
    # print(f"day = {day}")
    money = value[0]
    # print(f"money = {money}")
    heapq.heappush(ans, money)
    if day < len(ans):  # 해당 일자에 할 수 있는 일의 개수를 초과함. 최솟값 제거
        # print(f"len(ans) = {len(ans)}")
        # print(f"day = {day}")
        heapq.heappop(ans)
        # print(f"ans = {ans}")
    # print(f"ans = {ans}")
print(sum(ans))
