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
time = []
for i in range(n):
    start, end = map(int, input().split())
    time.append([start, end])
time.sort(key=lambda x: (x[1], x[0]))
print(f"time = {time}")
end_time = time[0][1]
cnt = 1
for idx in range(1, len(time)):
    if end_time <= time[idx][0]:
        print(f"end_time = {end_time}")
        print(f"ti[0] = {time[idx][0]}")
        cnt += 1
        end_time = time[idx][1]
print(cnt)
