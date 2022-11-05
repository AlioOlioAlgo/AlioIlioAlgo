"""
 *packageName    :
 * fileName       : 박상준
 * author         : ipeac
 * date           : 2022-11-04
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-11-04        ipeac       최초 생성
 """
# n, m, h = map(int, input().split())
# print(f"n, m, h = {n, m, h}")
# horizontal_line = []
# for i in range(m):
#     a, b = map(int, input().split())
#     horizontal_line.append([a, b])
#
# print(f"horizontal_line = {horizontal_line}")
# n ; 세로선의 개수 m ; 가로선 찎찍이 개수  h ; 가로선
c, m, r = (5, 5, 6)
ladder = [[0] * (c + 1) for _ in range(r + 1)]
# 가로선의 위치들 a번 점선의 위치 ;b번  b세로선과 b+1 세로선 ;
horizontal_line = [[1, 1], [3, 2], [2, 3], [5, 1], [5, 4]]
for ho in horizontal_line:
    ladder[ho[0]][ho[1]] = 1  # 가로선 시작점
    ladder[ho[0]][ho[1] + 1] = -1  # 가로선의 맞은편

# 출발점 시작점이 일치하는지 확인해야함
def check_start_end():
    for col in range(1, c + 1):
        start = col
        # 가로선을 만나는경우 1 인경우 col +1 처리해야함
        for row in range(1, r + 1):
            # 가로선이 1이라면 col +1 로 옆으로 이동시켜준다.
            if ladder[row][col] == 1:
                col += 1
            elif ladder[row][col] == -1:
                col -= 1
        
        if col != start:
            return False
    return True

#  line 만큼의 선을 그어가보면서 선택이 완료된다면 check호출로 결과 확인
def make_line(sr, sc, to_choose, line_cnt):  # 로우 ,컬럼, 남은 가로선 설치 가능 횟수  , 몇개 설치함?
    if to_choose == 0:
        if check_start_end():
            print(line_cnt)
            return True  # 답을 다 골랐으면 재귀돌 필요가 없어요
        return False  # 정답이 아닙니다 ㅠㅜㅠ
    for row in range(sr, r + 1):
        # 컬럼 마지막의 경우는 가로선을 별도로 추가할 이유가 없기에 c 앞까지만
        for col in range(sc, c):
            if ladder[row][col] == 0 and ladder[row][col + 1] == 0:
                ladder[row][col] = 1
                ladder[row][col + 1] = -1
                
                # 가지치기
                if make_line(row, col + 2, to_choose - 1, line_cnt):
                    return True
                    # 백트래킹
                ladder[row][col] = 0
                ladder[row][col + 1] = 0
        # row하나 체크완료
        # row가 변경되면 col 은 1부터 시작해야합니다.
        sc = 1
    return False

# 0~m개 까지의 가로선을 추가하면서 게임이 끝나는지 체크한다.
for i in range(m):
    # i 개수 만큼 가로선 추가하기
    result = make_line(1, 1, i, i)
    # true 라면
    if result:
        exit()

# 끝나지 않는 다면 게임이 망한거임
print(-1)
