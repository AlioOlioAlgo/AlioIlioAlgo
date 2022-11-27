"""
 *packageName    :
 * fileName       : Recursion
 * author         : ipeac
 * date           : 2022-11-27
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-11-27        ipeac       최초 생성
 """

def fac(n):
    if n == 1:
        return 1
    return n * fac(n - 1)

print(fac(n := int(input())))
# 단순연결 리스트 = 2. Add Two Number
