"""
 *packageName    : 
 * fileName       : 14499.주사위 굴리기
 * author         : ipeac
 * date           : 2023-03-16
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2023-03-16        ipeac       최초 생성
"""
n, m, x, y, k = map(int, input().split())

nums = [
    list(map(int, input().split()))
    for _ in range(n)
]
dx, dy = [0, 0, -1, 1], [1, -1, 0, 0]

# 인덱스 0 : 윗면
# 인덱스 1 ; 북
# 인덱스 2 ; 동
# 인덱스 3 ; 서
# 인덱스 4 : 남
# 인덱스 5 ; 아래
dice = [0] * 6  # 주사위

def roll_dice(input_dice, dir):
    global dice
    temp_dice = input_dice[:]
    if dir == 1:  # 동쪽
        input_dice[0] = temp_dice[3]
        input_dice[2] = temp_dice[0]
        input_dice[3] = temp_dice[5]
        input_dice[5] = temp_dice[2]
    elif dir == 2:  # 서쪽
        input_dice[3] = temp_dice[0]
        input_dice[0] = temp_dice[2]
        input_dice[2] = temp_dice[5]
        input_dice[5] = temp_dice[3]
    elif dir == 3:  # 북쪽
        input_dice[1] = temp_dice[0]
        input_dice[0] = temp_dice[4]
        input_dice[4] = temp_dice[5]
        input_dice[5] = temp_dice[1]
    elif dir == 4:  # 남쪽
        input_dice[4] = temp_dice[0]
        input_dice[0] = temp_dice[1]
        input_dice[5] = temp_dice[4]
        input_dice[1] = temp_dice[5]
    dice = input_dice[:]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

functions = list(map(int, input().split()))
# 동 1 서 2 북3 남 4

for fun in functions:
    nx, ny = x + dx[fun - 1], y + dy[fun - 1]
    if not in_range(nx, ny):
        continue
    x, y = nx, ny,
    roll_dice(dice, fun)
    # print(f"x, y,fun  ==> {x, y, fun}")
    # print(f"nums[x][y]  ==> {nums[x][y]}")
    # 주사위를 굴렸을 때, 이동한 칸에 쓰여 있는 수가 0이면, 주사위의 바닥면에 쓰여 있는 수가 칸에 복사된다.
    # 0이 아닌 경우에는 칸에 쓰여 있는 수가 주사위의 바닥면으로 복사되며, 칸에 쓰여 있는 수는 0이 된다.
    if nums[x][y] == 0:
        nums[x][y] = dice[5]
    elif nums[x][y] != 0:
        dice[5] = nums[x][y]
        nums[x][y] = 0
    print(dice[0])
