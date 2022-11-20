"""
 *packageName    :
 * fileName       : 구구다
 * author         : ipeac
 * date           : 2022-11-20
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-11-20        ipeac       최초 생성
 """
# 중복
for p in range(3):  # 1,2,3
    for i in range(1, 10):  # 1 to 9
        for j in range(p * 3 + 1, p * 3 + 4):  # j
            print(f'{j}x{i}={i * j}', end=" ")
        print()
    print()
