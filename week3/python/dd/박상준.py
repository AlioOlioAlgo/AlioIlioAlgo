"""
 *packageName    :
 * fileName       : 박상준
 * author         : ipeac
 * date           : 2022-11-10
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-11-10        ipeac       최초 생성
 """
# string = list(input())
string = 'we are flata'
ano = ['flatawe are ', 'tawe are fla', 'are flata']
for i in range(3):
    tmp = string
    flag = False
    for j in range(len(tmp)):
        tmp = (tmp[1:] + tmp[0])
        if tmp == ano[i]:
            print(True)
            flag = True
            break
    if not flag:
        print(False)
