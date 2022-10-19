"""
 *packageName    : 
 * fileName       : 박상준
 * author         : ipeac
 * date           : 2022-10-19
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-10-19        ipeac       최초 생성
 """
from itertools import combinations

s_height = [
    int(input())
    for _ in range(9)
]
# 난쟁이들의 키를 받습니다.
# 
# s_height = [20, 7, 23, 19, 10, 15, 25, 8, 13]
# 
# 콤비네이션 처리 7마리 골라내고
for combi in combinations(s_height, 7):
    # combi 의 합계값이 100 인경우 tuple -> list 전환 후 sorted 함수로 오름차순 정렬
    if sum(combi) == 100:
        combi = sorted(list(combi))
        # 출력
        for value in combi:
            print(value)
        # 강제 종료
        exit()

#  시간 복잡도 : n! / r! / (n - r)!
