"""
 *packageName    : 
 * fileName       : 박상준2
 * author         : ipeac
 * date           : 2022-10-27
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-10-27        ipeac       최초 생성
 """
from collections import defaultdict

t = int(input())
while t:
    t -= 1
    n = int(input())
    dic = defaultdict(int)
    for i in range(n):
        cloth, kind = map(str, input().split())
        dic[kind] += 1
    # n = 3
    # dic = {'headgear': 2, 'eyewear': 1}
    # print(f"dic = {dic}")
    ans = 1
    
    for value in dic.values():
        ans *= value + 1
    print(ans - 1)  # 모든 경우의 수 - 모든 옷을 안입는 행위 1가지
