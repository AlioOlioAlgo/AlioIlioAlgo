"""
 *packageName    :
 * fileName       : 박상준
 * author         : ipeac
 * date           : 2022-11-08
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-11-08        ipeac       최초 생성
 """
from collections import deque

t = int(input())
# t = 4
for _ in range(t):
    # print(f"t = {t}")
    function = deque(list(map(str, input())))
    # print(f"function = {function}")
    n = int(input())
    #     print(f"n = {n}")
    int_arr = deque(input().rstrip()[1:-1].split(","))
    #     print(f"int_arr = {int_arr}")
    # function = deque(['R', 'D', 'D'])
    # n = 4
    # int_arr = deque(['1', '2', '3', '4'])
    # 첫번째 수를 버리는 경우 pop() <- 결국 리스트 순회
    # 뒤집는 경우 <- 결국 리스트 순회
    #  100,000 **  100,000
    # 다른 방법으로
    flag = True  # 마지막 조건 분기
    reverse_count = 0
    if n == 0:
        int_arr = []
    
    for func in function:
        if func == 'R':
            reverse_count += 1
        elif func == 'D':
            if len(int_arr) < 1:
                print('error')
                flag = False
                break
            else:  # 길이가 1이상인 경우
                # 만약 r 이 짝수인 경우 본래의 숫자에서 앞부분
                if reverse_count % 2 == 0:
                    int_arr.popleft()
                else:  # 홀수인 경우 이미 뒤집힌 상태니까 뒷 부분
                    int_arr.pop()
    if flag:  # 리버스 카운트
        if reverse_count % 2 == 0:
            pass
        else:
            int_arr.reverse()
        # 무조건 에러나면 안된다.
        print('[' + ','.join(int_arr) + ']')
