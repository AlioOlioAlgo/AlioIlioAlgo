"""
 *packageName    :
 * fileName       : 박상준
 * author         : ipeac
 * date           : 2022-11-06
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-11-06        ipeac       최초 생성
 """
n = int(input())
if n == 0:
    print(1)
elif n >= 1:
    print(len(bin(n)[2:]))
else:  # 최대 31비트 까지 가용 -> 제일 앞쪽에 부호비트가 1 이라서.. + 32비트로 적용됨
    print(32)
