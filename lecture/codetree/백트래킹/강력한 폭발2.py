"""
 *packageName    :
 * fileName       : 강력한 폭발2
 * author         : ipeac
 * date           : 2023-01-29
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2023-01-29        ipeac       최초 생성
 """
n = int(input())
graph = [
]
bomb_map = [
    [],
    [[-1, 0], [1, 0], [0, 0], [-2, 0], [2, 0]],
    [[-1, 0], [1, 0], [0, 0], [0, 1], [0, -1]],
    [[-1, -1], [1, 1], [0, 0], [1, -1], [-1, 1]]
]
bomb_cnt = 0
bomb_index = []

for i in range(n):
    line_man = list(map(int, input().split()))
    for j in range(n):
        if line_man[j] == 1:
            bomb_cnt += 1
            bomb_index.append([i, j])
    graph.append(line_man)

print(f"bomb_cnt = {bomb_cnt}")
print(f"graph = {graph}")

max_cnt = -1e9

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

bomb_location = [
    [False for _ in range(n)]
    for _ in range(n)
]

def bomb(x, y, type):  # 폭탄을 떨어뜨립니다.
    for i in range(5):
        dx, dy = bomb_map[type][i]
        nx, ny = x + dx, y + dy
        if in_range(nx, ny):
            bomb_location[nx][ny] = True

def calc():  # 폭탄수 카운트
    for i in range(n):
        for j in range(n):
            bomb_location[i][j] = False  # 폭탄의 위치를 초기화함.
    
    for i in range(n):
        for j in range(n):
            if bomb_take[i][j]:
                bomb(i, j, bomb_take[i][j])
    
    ans = 0  # 폭탄 터진 위치를 1로 계산후 count()
    for i in range(n):
        for j in range(n):
            if bomb_location[i][j]:
                ans += 1
    return ans

bomb_take = [
    [0 for _ in range(n)]
    for _ in range(n)
]

def make(cnt):
    global max_cnt
    if cnt == bomb_cnt:
        max_cnt = max(max_cnt, calc())
        return
    for i in range(1, 4):
        x, y = bomb_index[cnt]
        bomb_take[x][y] = i  # 일단 1~3의 수를 임의 세팅
        make(cnt + 1)
        bomb_take[x][y] = 0  # 초기화

make(0)
print(max_cnt)
