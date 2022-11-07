"""
 *packageName    :
 * fileName       : 박상준
 * author         : ipeac
 * date           : 2022-11-07
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-11-07        ipeac       최초 생성
 """

s = input()
while s:
    if s[0:2] == 'pi':
        s = s[2:]
        pass
    elif s[0:2] == 'ka':
        s = s[2:]
        pass
    elif s[0:3] == 'chu':
        s = s[3:]
        pass
    else:
        print('NO')
        exit()
print('YES')
