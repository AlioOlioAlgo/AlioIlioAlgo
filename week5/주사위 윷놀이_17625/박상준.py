"""
 *packageName    :
 * fileName       : 박상준
 * author         : ipeac
 * date           : 2022-12-16
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-12-16        ipeac       최초 생성
 """
grid_dict = {
    0: [1, 2, 3, 4, 5],
    1: [2, 3, 4, 5, 6],
    2: [3, 4, 5, 6, 7],
    3: [4, 5, 6, 7, 8],
    4: [5, 6, 7, 8, 9],
    5: [21, 22, 23, 24, 25],
    6: [7, 8, 9, 10, 11],
    7: [8, 9, 10, 11, 12],
    8: [9, 10, 11, 12, 13],
    9: [10, 11, 12, 13, 14],
    10: [27, 28, 24, 25, 26],
    11: [12, 13, 14, 15, 16],
    12: [13, 14, 15, 16, 17],
    13: [14, 15, 16, 17, 18],
    14: [15, 16, 17, 18, 19],
    15: [29, 30, 31, 24, 25],
    16: [17, 18, 19, 20, -1],
    17: [18, 19, 20, -1, -1],
    18: [19, 20, -1, -1, -1],
    19: [20, -1, -1, -1, -1],
    20: [-1, -1, -1, -1, -1],
    21: [22, 23, 24, 25, 26],
    22: [23, 24, 25, 26, 20],
    23: [24, 25, 26, 20, -1],
    24: [25, 26, 20, -1, -1],
    25: [26, 20, -1, -1, -1],
    26: [20, -1, -1, -1, -1],
    27: [28, 24, 25, 26, 20],
    28: [24, 25, 26, 20, -1],
    29: [30, 31, 24, 25, 26],
    30: [31, 24, 25, 26, 20],
    31: [24, 25, 26, 20, -1]
}
score_dict = {  # 인덱스에 맞는 점수를 이어준다.
    -1: 0, 0: 0, 1: 2, 2: 4, 3: 6, 4: 8, 5: 10, 6: 12, 7: 14, 8: 16, 9: 18, 10: 20,
    11: 22, 12: 24, 13: 26, 14: 28, 15: 30, 16: 32, 17: 34, 18: 36, 19: 38, 20: 40, 21: 13, 22: 16,
    23: 19, 24: 25, 25: 30, 26: 35, 27: 22, 28: 24, 29: 28, 30: 27, 31: 26
}
answer = 0
dice = list(map(int, input().split()))

state = [0, 0, 0, 0]  # 주사위 마다의 위치 기록용

def go(horse, count, result, state):
    global grid_dict, score_dict, answer, dice
    copy_state = state[:]
    now_dice = dice[count] - 1
    copy_state[horse] = grid_dict[copy_state[horse]][now_dice]
    now_score = score_dict[copy_state[horse]]
    
    if count == 9:
        answer = max(answer, result + now_score)
        return
    
    next_dice = dice[count + 1] - 1
    for i in range(4):
        if copy_state[i] == -1:  # 도착한 경우
            continue
        if grid_dict[copy_state[i]][next_dice] != -1 and grid_dict[copy_state[i]][next_dice] in copy_state:
            continue
        go(i, count + 1, result + now_score, copy_state)

go(0, 0, 0, state)
print(answer)
