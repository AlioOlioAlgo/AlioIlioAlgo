"""
 *packageName    : 
 * fileName       : 박상준
 * author         : ipeac
 * date           : 2022-10-24
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-10-24        ipeac       최초 생성
 """

t = int(input())
for _ in range(t):
    gg = list(map(str, input()))
    
    cnt = 0
    for g in gg:
        if g == '(':
            cnt += 1
        else:
            cnt -= 1
            if cnt < 0:
                print('NO')
                break
    if cnt == 0:
        print('YES')
    elif cnt > 0:
        print('NO')
