"""
 *packageName    : 
 * fileName       : 박상주
 * author         : ipeac
 * date           : 2022-10-24
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-10-24        ipeac       최초 생성
 """
n = int(input())
word = 666
cnt = 0
while 1:
    if '666' in str(word):
        cnt += 1
    if cnt == n:
        print(word)
        break
    word += 1
