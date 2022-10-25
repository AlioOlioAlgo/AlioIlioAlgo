"""
 *packageName    : 
 * fileName       : 박상준
 * author         : ipeac
 * date           : 2022-10-23
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-10-23        ipeac       최초 생성
 """
h, w = map(int, input().split())
sky = [
    list(map(str, input()))
    for _ in range(h)
]
# print(f"h,w = {h, w}")
# print(f"sky = {sky}")

# h, w = (3, 4)
# sky = [['c', '.', '.', 'c'], ['.', '.', 'c', '.'], ['.', '.', '.', '.']]
for sk in sky:
    sky_chk = False
    i = 0
    for s in sk:
        if s == 'c':
            sky_chk = True
        if not sky_chk:
            print(-1, end=" ")
        else:
            if s == 'c':
                print(0, end=" ")
                i = 0
            else:
                i += 1
                print(i, end=" ")
    print()
