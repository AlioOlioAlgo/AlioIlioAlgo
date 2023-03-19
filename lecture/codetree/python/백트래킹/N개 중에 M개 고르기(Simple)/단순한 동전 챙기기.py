"""
 *packageName    :
 * fileName       : 단순한 동전 챙기기
 * author         : ipeac
 * date           : 2023-02-02
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2023-02-02        ipeac       최초 생성
 """
n = int(input())
graph = [
]
back_track = []
number_list = {}
start_index = 0
end_index = 0

for i in range(n):
    line_input = list(map(str, input()))
    for j in range(n):
        if line_input[j].isnumeric():
            number_list[int(line_input[j])] = [i, j]
        elif line_input[j] == "S":
            start_index = [i, j]
        elif line_input[j] == "E":
            end_index = [i, j]
print(f"number_list = {number_list}")
print(f"start_index = {start_index}")
print(f"end_index = {end_index}")

min_value = 1e9

# 최소 3개의 동전을 수집해 목적지로 이동합니다.
def calc():
    print(f"back_track = {back_track}")
    value = 0
    tmp_x = start_index
    tmp_y = end_index
    for back_value in back_track:
        value += diff(number_list[back_value][0], tmp_x, number_list[back_value][1], tmp_y)
        tmp_x, tmp_y = number_list[back_value][0], number_list[back_value][1]
    
    return value

def diff(x1, y1, x2, y2):
    return abs(x2 - x1) + abs(y2 - y1)

def move(choose_num, cnt):
    global min_value
    if cnt == 3:
        min_value = min(min_value, calc())
        return
    for i in range(choose_num + 1, 10):
        back_track.append(i)
        move(i, cnt + 1)
        back_track.pop()

move(0, 0)
