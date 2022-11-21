"""
 *packageName    :
 * fileName       : 1
 * author         : ipeac
 * date           : 2022-11-20
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-11-20        ipeac       최초 생성
 """
while True:
    print("==========================================")
    n = int(input())  # 10
    if n == 99999:
        exit()
    star = 1
    blank = n
    for i in range(n):
        for k in range(blank):
            print(' ', end=" ")
        for j in range(star):
            print('*', end=" ")
        print()
        
        blank -= 1
        star += 1
