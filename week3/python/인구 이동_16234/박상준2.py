"""
 *packageName    :
 * fileName       : 박상준2
 * author         : ipeac
 * date           : 2022-11-19
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-11-19        ipeac       최초 생성
 """
N, L, R = map(int, input().split())
# n 각 나라의 인구수
# 각 나라의 인구 차이가 L이상 R이하라면 두 도시의 국경선을 오픈
# 모든 국경선을 열고, 인구 이동을 시작한다.
# 국경선 오픈 하루 동안 연합임
# 연합을 이루는 인구수 ( 연합 인구 ) / ( 연합을 이루는 칸의 개수)
# 연합 해제 >국경선 닫음

# 각 나라의 인구수가 주어졌을 때, 인구 이동이 며칠 동안 발생하는지 구하는 프로그램을 작성하시오.
while True:
    visited = [[0] * N for _ in range(N)]
    
    for i in range(N):
        for j in range(N):
    
    pass
