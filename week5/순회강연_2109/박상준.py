"""
 *packageName    :
 * fileName       : 박상준
 * author         : ipeac
 * date           : 2022-11-17
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-11-17        ipeac       최초 생성
 """
from queue import PriorityQueue

n = int(input())
list_a = []
for i in range(n):
    p, d = map(int, input().split())
    list_a.append([p, d])
list_a.sort(key=lambda x: x[1])
# print(f"list_a = {list_a}")
ans = PriorityQueue()
for value in list_a:
    day = value[1]
    money = value[0]
    
    ans.put(money)
    
    if day < ans.qsize():
        ans.get()

print(sum(ans.queue))
