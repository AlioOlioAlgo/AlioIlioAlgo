"""
 *packageName    : 
 * fileName       : Fly me to the Alpha Centauri
 * author         : ipeac
 * date           : 2023-03-06
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2023-03-06        ipeac       최초 생성
"""
n = int(input())

for i in range(n):
    x, y = map(int, input().split())
    if abs(x - y) == 1:
        print(1)
        continue
    if abs(x - y) == 2:
        print(2)
        continue
    cnt = 0
    plus_num = 2
    x += 1
    y -= 1
    while True:
        x += plus_num
        cnt += 1
        plus_num += 1
        if x >= y:
            break
    print(cnt + 2)
