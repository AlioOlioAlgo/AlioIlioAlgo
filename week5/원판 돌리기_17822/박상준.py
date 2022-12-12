"""
 *packageName    :
 * fileName       : 박상준
 * author         : ipeac
 * date           : 2022-12-10
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-12-10        ipeac       최초 생성
 """
from collections import deque

n, m, t = map(int, input().split())  #

# n 개 줄에 원판에 적힌 수가 주어진다.
one_pan = [
    deque(list(map(int, input().split())))
    for _ in range(n)
]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# 원판 특정값에서 같은 숫자를 탐색합니다.
def find_same_number(i, j, one_pan):
    q = deque()
    q.append([i, j])
    number = one_pan[i][j]
    visited = []
    
    while q:
        x, y = q.popleft()
        print(f"x, y = {x, y}")
        for o in range(4):
            nx, ny = x + dx[o], y + dy[o]
            
            if ny == m:
                ny = 0
            if ny < 0:
                ny = m - 1
            
            # 원판 확인 . 기준값과 원판의 값이 동일하다면, 방문여부 체크
            if 0 <= nx < n and one_pan[nx][ny] == number and [nx, ny] not in visited:
                q.append([nx, ny])
                visited.append([nx, ny])
    return visited

# t 만큼회전합니다.
for _ in range(t):
    x, d, k = map(int, input().split())  # x 배수인 원판을 d 방향으로 k 만큼 회전한다.
    while x <= len(one_pan):
        print(f"x = {x}")
        # x 배수의 원판을 회전시킨다.
        if d == 1:  # 1 이라면 반시계 방향 회전
            one_pan[x - 1].rotate(-k)
        else:  # 0  이라면 시계 방향 회전
            one_pan[x - 1].rotate(k)
        x += x
    print(f"one_pan = {one_pan}")
    
    # 인접한 값을 확인한다.
    is_adj = False
    for i in range(n):
        for j in range(m):
            if one_pan[i][j] == 0:  # same number 처리가 되었다면 무시하고 진행
                continue
            erase = find_same_number(i, j, one_pan)
            
            if erase:
                is_adj = True
                for tx, ty, in erase:
                    one_pan[tx][ty] = 0
                # 현재 비교 기준값도 0 으로 변경시킨다.
                one_pan[i][j] = 0
    print(f"one_pan = {one_pan}")
    
    # 인접하면서 같은 수가 없는 경우
    if not is_adj:
        # 원판에 적힌 수의 평균을 구하고, 평균에서 큰수는 -1 , 작은수 +1
        sum_one = sum(map(sum, one_pan))
        zero_cnt = 0
        tmp_line_arr = map(list, one_pan)
        for line in tmp_line_arr:
            zero_cnt += line.count(0)
        division_cnt = n * m - zero_cnt
        if division_cnt == 0:
            continue
        avg_one = sum_one / division_cnt  # 평균값
        
        for i in range(n):
            for j in range(m):
                if one_pan[i][j] != 0:
                    if one_pan[i][j] < avg_one:
                        one_pan[i][j] += 1
                    elif one_pan[i][j] > avg_one:
                        one_pan[i][j] -= 1
        print(f"원판 평균 조정값 = {one_pan}")
print(sum(map(sum, one_pan)))
