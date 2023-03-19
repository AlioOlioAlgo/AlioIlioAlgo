"""
 *packageName    : 
 * fileName       : 문제 추천 시스템1
 * author         : ipeac
 * date           : 2023-02-24
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2023-02-24        ipeac       최초 생성
"""
import bisect

n = int(input())
matters = []
for i in range(n):
    p, l = map(int, input().split())
    bisect.insort(matters, (l, p))
m = int(input())
for i in range(m):
    function = list(map(str, input().split()))
    if function[0] == "ad":  # 난이도가 L인 문제번호 P를 추가합니다.
        bisect.insort(matters, (int(function[2]), int(function[1])))
    elif function[0] == "sv":  # 난이도가 L인 문제 번호 P 를 제거합니다.
        matters.remove((int(function[2]), int(function[1])))
    else:  # rc  x x 가 1인 경우 난이도가 가장 높음 -1 인 경우 난이도가 가장 낮은 문제의 번호 출력 -> 난이도가 가장 낮은 문제가 여러 개라면 문제 번호가 작은 것으로 출력합니다.
        x = int(function[1])
        print(matters[0][1]) if x == -1 else print(matters[-1][1])
