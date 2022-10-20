"""
 *packageName    : 
 * fileName       : 박상준
 * author         : ipeac
 * date           : 2022-10-20
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-10-20        ipeac       최초 생성
 """
import sys
from collections import defaultdict

input = sys.stdin.readline
t = int(input().rstrip())

for i in range(t):
    n = int(input().rstrip())
    clothes = defaultdict(int)
    
    sum_value = 1
    
    # 의상의 이름 , 종류
    for i in range(n):
        name, kind, = map(str, input().rstrip().split())
        clothes[kind] += 1
    # 종류가 2 1 개면 각각 한개씩 선택할수 있는 경우의 수 +1 => 각각 종류에서 조합할 수있는 수+1 => 3 *2 값에서 아무것도 안입는 경우 -1
    for value in clothes.values():
        sum_value *= value + 1
    print(sum_value - 1)
