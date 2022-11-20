"""
 *packageName    :
 * fileName       : 박상준
 * author         : ipeac
 * date           : 2022-11-20
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-11-20        ipeac       최초 생성
 """
n = int(input())
cow = []
for i in range(n):
    arrived, check_cow = map(int, input().split())
    cow.append([arrived, check_cow])
cow.sort(key=lambda x: x[0])
# print(f"cow = {cow}")
now = cow[0][0] + cow[0][1]
# print(f"now = {now}")

for idx in range(1, len(cow)):
    # print(f"now = {now}")
    while cow[idx][0] > now:
        now += 1
    
    now += cow[idx][1]
print(now)
