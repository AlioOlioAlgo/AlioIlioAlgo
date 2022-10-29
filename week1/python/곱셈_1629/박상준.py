"""
 *packageName    : 
 * fileName       : 박상준
 * author         : ipeac
 * date           : 2022-10-22
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-10-22        ipeac       최초 생성
 """
a, b, c = map(int, input().split())

# 분할정복을 이용한 거듭제곱
def power(a, n):
    if n == 0:
        return 1
    x = power(a, n // 2)
    if n % 2 == 0:
        return x * x % c
    else:
        return x * x * a % c

print(power(a, b))  # 10 11 12
