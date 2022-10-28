"""
 *packageName    : 
 * fileName       : 박상준2
 * author         : ipeac
 * date           : 2022-10-28
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-10-28        ipeac       최초 생성
 """
n = int(input())
score_list = [
    list(map(str, input().split()))
    for _ in range(n)
]
#
score_list.append(['-1', '48:00'])

# print(f"n = {n}")
# print(f"score_list = {score_list}")

# n = 5
# score_list = [['1', '01:10'], ['1', '02:20'], ['2', '45:30'], ['2', '46:40'], ['2', '47:50'], ['-1', '48:00']]

first = 0
second = 0
first_time = 0
second_time = 0
idx = 0
for team, time in score_list:
    hour, minute = map(int, time.split(":"))
    pre_hour, pre_minute = map(int, score_list[idx - 1][1].split(":"))
    if first > second:
        first_time += (60 * hour) - (60 * pre_hour) + (minute - pre_minute)
    elif first < second:
        print(f"hour = {hour, minute}")
        print(f"pre_hour = {pre_hour, pre_minute}")
        second_time += (60 * hour) - (60 * pre_hour) + (minute - pre_minute)
    
    if team == '1':
        first += 1
    elif team == '2':
        second += 1
    idx += 1
print(f'{str(first_time // 60).zfill(2)}:{str(first_time % 60).zfill(2)}')
print(f'{str(second_time // 60).zfill(2)}:{str(second_time % 60).zfill(2)}')
