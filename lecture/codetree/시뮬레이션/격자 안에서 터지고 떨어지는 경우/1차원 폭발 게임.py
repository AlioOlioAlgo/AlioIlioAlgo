"""
 *packageName    :
 * fileName       : 1차원 폭발 게임
 * author         : ipeac
 * date           : 2023-01-04
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2023-01-04        ipeac       최초 생성
 """
n, m = map(int, input().split())
boom_list = [
    int(input())
    for _ in range(n)
]
print(f"boom_list = {boom_list}")
trigger = True
while trigger:
    tmp_boom = boom_list[:]
    if len(boom_list):
        first = boom_list[0]
        cnt = 1
        
        for i in range(1, len(boom_list)):
            if first == boom_list[i]:
                cnt += 1
                if cnt >= m:
                    pass
    else:
        break
