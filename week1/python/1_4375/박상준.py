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
while True:
    try:
        n = int(input())
    except:
        break
    ans = 1
    i = 1
    if n == 1:
        print(i)
        continue
    # 시간 초과가 발생했었음
    # str => int int => str 변환하는데에  시간이 소요된 것으로 생각..
    # 그냥 *10 곱해주고 +1 하는 식으로 int 형 안에서 해결을 해야했다
    while True:
        i += 1
        ans = ans * 10 + 1
        if ans % n == 0:
            print(i)
            break
