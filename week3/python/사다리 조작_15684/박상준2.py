"""
 *packageName    :
 * fileName       : 박상준2
 * author         : ipeac
 * date           : 2022-11-05
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-11-05        ipeac       최초 생성
 """
# c ; 세로선의 개수 m ; 가로선 찎찍이 개수  r ; 가로선
c, m, r = (5, 5, 6)
ladder = [[0] * (c + 1) for _ in range(r + 1)]
# 가로선의 위치들 a번 점선의 위치 ;b번  b세로선과 b+1 세로선 ;
horizontal_line = [[1, 1], [3, 2], [2, 3], [5, 1], [5, 4]]
for ho in horizontal_line:
    ladder[ho[0]][ho[1]] = 1  # 가로선의 시작점
    ladder[ho[0]][ho[1] + 1] = -1  # 가로선의 맞은편

# 출발점과 시작점이 일치하는지 검증한다,.
def start_end_ok():
    for col in range(1, c + 1):
        start = col
        for row in range(1, r + 1):
            # 가로선을 만나는 경우 col+1 처리되어야함
            if ladder[row][col] == 1:
                col += 1
            elif ladder[row][col] == -1:
                col -= 1
        # 처음 시작점과 끝점이 다르다면 `FALSE` 처리
        if col != start:
            return False
    # 처음 시작점과 끝점이 같아면 `TRUE` 처리
    return True

# line 만큼의 선을 그어보면서 선택이 완료된다면 check호출로 결과 확인
def make_line(start_row, start_col, to_choose, line_cnt):
    # row col 현재 위치 || 남은 가로선 설치 횟수 ||몇개를 설치했는지
    if to_choose == 0:
        # 만약 가로선 설치 횟수가 0 이라면 이제 더 이상 가로선을 둘수없다.
        if start_end_ok():
            # 만약 시작점과 끝점이 동일하다면
            # 현재까지 설치한 가로선의 개수를 프린트
            print(line_cnt)
            return True
    for row in range(start_row, r + 1):
        for col in range(start_col, c):
            # 사다리 현재 위치의 값이 0이며 그 다음 값도 0이여야함 > 가로선이 연속할 수 없기때문
            if ladder[row][col] == 0 and ladder[row][col + 1] == 0:
                ladder[row][col] = 1
                ladder[row][col + 1] = -1
                
                # 가지치기
                if make_line(start_row, start_col + 2, to_choose - 1, line_cnt):
                    return True

# 0~ m 개의 가로선을 놓아서 게임이 끝나는지 체크한다.
for i in range(m):
    result = make_line(1, 1, i, i)
    if result:
        exit()
print(-1)
